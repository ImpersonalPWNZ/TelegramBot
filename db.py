import psycopg2
import json

def getUsers():
    connection = psycopg2.connect(user="postgres",
                                  password="12345",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="PointShop")
    cursor = connection.cursor()
    querry = f""" SELECT * FROM public."users" """
    cursor.execute(querry)
    cursor.close()
    connection.close()
    return json.dumps(cursor.fetchall())
def checkPhoto(id):
    connection = psycopg2.connect(user="postgres",
                                  password="12345",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="PointShop")
    cursor = connection.cursor()
    querry = f""" SELECT "photo" FROM public."Items" WHERE "Id" = {id}"""
    cursor.execute(querry)
    if cursor.fetchone() is None:
        res = True;
    else:
        res = False;
    cursor.close()
    connection.close()
    return res
def addPhoto(id,link):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="12345",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="PointShop")
        cursor = connection.cursor()
        insert_querry = f""" UPDATE public.Items SET photo = {link} WHERE "Id" = {id}"""
        cursor.execute(insert_querry)
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
def getItemInfo(id):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="12345",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="PointShop")
        cursor = connection.cursor()
        querry = f""" SELECT * FROM public."Items" WHERE "Id" = {id} """
        cursor.execute(querry)
        info = cursor.fetchone()
        print(info)
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            return info
def getItemCount():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="12345",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="PointShop")
        cursor = connection.cursor()
        querry = f""" SELECT COUNT(*) FROM public."Items" """
        cursor.execute(querry)
        info = cursor.fetchone()
        print(info)
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            return info
def getInfo(tgID):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="12345",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="PointShop")
        cursor = connection.cursor()
        querry = f""" SELECT * FROM public."users" WHERE "telegramID" = {tgID} """
        cursor.execute(querry)
        info = cursor.fetchone()
        print(info)
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            return info
def checkUser(tgID):
        connection = psycopg2.connect(user="postgres",
                                      password="12345",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="PointShop")
        cursor = connection.cursor()
        querry = f""" SELECT * FROM public."users" WHERE "telegramID" = {tgID}"""
        cursor.execute(querry)
        if cursor.fetchone() is None:
            res = False;
        else:
            res = True;
        cursor.close()
        connection.close()
        return res
def addItem(name,price,count):
    try:
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password="12345",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="PointShop")
        cursor = connection.cursor()
        insert_querry = """ INSERT INTO public."Items" ("Name", "Price", "Count") VALUES (%s,%s,%s)"""
        record_to_insert =(name,price,count)
        cursor.execute(insert_querry,record_to_insert)
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
def addUser(tID,points,FIO):
    try:

        connection = psycopg2.connect(user="postgres",
                                      password="12345",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="PointShop")
        cursor = connection.cursor()
        insert_querry = f""" INSERT INTO public."users" ("telegramID", "points", "fio") VALUES ({tID},{points},'{FIO}')"""
        cursor.execute(insert_querry)

        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
def deleteItembyName(name):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="12345",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="PointShop")
        cursor = connection.cursor()
        delete_querry = f""" DELETE FROM public."Items" WHERE "Name" = '{name}'"""
        cursor.execute(delete_querry)
        print(f"Успешно удален элемент из таблицы таблицу Items с именем {name}")
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
def deleteUserbyTGID(tgID):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="12345",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="PointShop")
        cursor = connection.cursor()
        delete_querry = f""" DELETE FROM public."users" WHERE "telegramID" = '{tgID}'"""
        cursor.execute(delete_querry)
        print(f"Успешно удален элемент из таблицы таблицу USERS с tgID {tgID}")
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
def deleteUserbyFIO(FIO):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="12345",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="PointShop")
        cursor = connection.cursor()
        delete_querry = f""" DELETE FROM public."users" WHERE "fio" = '{FIO}'"""
        cursor.execute(delete_querry)
        print(f"Успешно удален элемент из таблицы таблицу USERS с ФИО {FIO}")
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
def updatePointsByTGID(c,tgID):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="12345",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="PointShop")
        cursor = connection.cursor()
        print(c)
        update_querry = f"""UPDATE public.users SET points = points+{c} WHERE "telegramID" = {tgID}"""
        print(update_querry)
        cursor.execute(update_querry)
        print(f"Баланс {tgID} успешно изменен на {c}")
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
def subItemCount(id):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="12345",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="PointShop")
        cursor = connection.cursor()
        update_querry = f"""UPDATE public."Items" SET "Count"="Count"-1 WHERE "Id" = '{id}'"""
        print(update_querry)
        cursor.execute(update_querry)
        print(f'{id} count -1')
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
def buyThing(tgID,id):
    try:
        connection = psycopg2.connect(user="postgres",

                                      password="12345",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="PointShop")
        cursor = connection.cursor()
        querry = f""" SELECT "points" FROM public."users" WHERE "telegramID" = {tgID}"""
        cursor.execute(querry)
        points = cursor.fetchone()
        points = points[0]
        querry = f""" SELECT "Price"::integer FROM public."Items" WHERE "Id" = '{id}'"""
        cursor.execute(querry)
        price = cursor.fetchone()
        price = -price[0]
        querry = f""" SELECT "Count"::integer FROM public."Items" WHERE "Id" = '{id}'"""
        cursor.execute(querry)
        count = cursor.fetchone()
        if count[0] == 0:
            cor = False
        else:
            if points >= price:
                subItemCount(id)
                updatePointsByTGID(price,tgID)
                cor = True
            else:
                cor = False
            connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            return cor