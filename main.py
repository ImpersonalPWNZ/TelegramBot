
import db
import asyncio
import config
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.middlewares.logging import LoggingMiddleware
loop = asyncio.get_event_loop()

bot = Bot(token=config.TOKEN, loop=loop, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

class buy(StatesGroup):
    buy = State()
class fio(StatesGroup):
    fio = State()
    text = ''

def welcome_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=cb) for name, cb in
                   {'Вход': 'ENTER'}.items()])
    keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=cb) for name, cb in
                   {'Регистрация': 'REG'}.items()])
    return keyboard

def main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=cb) for name, cb in
                   {'Информация': 'INF'}.items()])
    keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=cb) for name, cb in
                   {'Каталог': 'T'}.items()])
    return keyboard

@dp.message_handler(commands=['start'])
async def process_start_command(m: types.Message):
    await bot.send_message(m.chat.id, "Зарегистрируйтесь либо авторизуйтесь", reply_markup=welcome_keyboard())

@dp.message_handler(state=fio.fio)
async def input_report(m: types.Message, state: FSMContext):
    db.addUser(m.chat.id, 100, m.text)
    await bot.send_message(m.chat.id, f'Успешная регистрация')
    await state.finish()

@dp.message_handler(state=buy.buy)
async def input_report(m: types.Message, state: FSMContext):
    cor = db.buyThing(m.chat.id, m.text)
    if cor == True:
        await bot.send_message(m.chat.id, f'Успешная покупка')
    else:
        await bot.send_message(m.chat.id, 'Товар отсутвутет либо недостаточно средств для покупки')
    await state.finish()

@dp.callback_query_handler(lambda c: c.data, state="*")
async def poc_callback_but(c:types.CallbackQuery, state: FSMContext):
    m = c.message
    if 'BUY' == c.data:
        await bot.send_message(m.chat.id,'Для подтверждения введите номер товара')
        await buy.first()
    if 'REG' == c.data:
        await bot.send_message(m.chat.id, 'Введите свое ФИО')
        await fio.first()

@dp.message_handler(content_types='text', state="*")
async def echo_message(m: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    if m.text == 'Регистрация':
        check = db.checkUser(m.chat.id)
        if check == False:
            keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=cb) for name, cb in
                           {'Регистрация': 'REG'}.items()])
            await bot.send_message(m.chat.id, 'Нажмите кнопку ниже.', reply_markup=keyboard)
        else:
            await bot.send_message(m.chat.id, 'Уже зарегистрирован.', reply_markup=keyboard)
    elif m.text == 'Вход':
        check = db.checkUser(m.chat.id)
        if check == False:
            await bot.send_message(m.chat.id, 'Сначала пройдите регистрацию.', reply_markup=keyboard)
        else:
            await bot.send_message(m.chat.id, 'Успешная авторизация.', reply_markup=main_keyboard())
    elif m.text =='Информация':
        info = db.getInfo(m.chat.id)
        await bot.send_message(m.chat.id,f' tgID = {info[0]}\nКоличество очков = {info[1]}\nФИО = {info[2]}', reply_markup=main_keyboard())
    elif m.text =='Каталог':
        Count = db.getItemCount()
        Count = Count[0]
        print(f"item count {Count}")
        i=1
        while i<=Count:
            keyboard = types.InlineKeyboardMarkup()
            info = db.getItemInfo(i)
            keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=cb) for name, cb in
                           {'Купить': 'BUY'}.items()])
            if info[4] == None:
                await bot.send_message(m.chat.id,f'Номер товара {info[3]}\nНаименование товара - {info[0]}\nСтоимость товара = {info[1]}\nОставшееся количество {info[2]}', reply_markup=keyboard)
            else:
                await bot.send_photo(m.chat.id,photo=info[4],caption=f'Номер товара {info[3]}\nНаименование товара - {info[0]}\nСтоимость товара = {info[1]}\nОставшееся количество {info[2]}', reply_markup=keyboard)
            i = i + 1

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)