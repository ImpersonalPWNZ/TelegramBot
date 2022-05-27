from flask import Flask, jsonify
import bytes
from flask_restful import Api, Resource
import psycopg2
import base64
app = Flask(__name__)
api = Api()

@app.route('/setphoto/<int:id>&<string:link1>', methods=['PUT'])
def setphoto(id,link1):
    link = base64.urlsafe_b64decode(link1)
    link = link.decode("utf-8")
    connection = psycopg2.connect(user="postgres",
                                  password="12345",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="PointShop")
    cursor = connection.cursor()
    update_query = f"""UPDATE public."Items" SET photo = '{link}' WHERE "Id" = {id}"""
    cursor.execute(update_query)
    connection.commit()
    return getitems()
@app.route('/setpoints/<int:id>&<int:c>', methods=['PUT'])
def setpoints(id,c):
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="12345",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="PointShop")
    cursor = connection.cursor()
    update_query = f"""UPDATE public.users SET points = {c} WHERE "id" = {id}"""
    cursor.execute(update_query)
    connection.commit()
    return getusers()
@app.route('/subpoints/<int:id>&<int:c>', methods=['PUT'])
def subpoints(id,c):
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="12345",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="PointShop")
    cursor = connection.cursor()

    update_query = f"""UPDATE public.users SET points = points-{c} WHERE "id" = {id}"""
    cursor.execute(update_query)
    connection.commit()
    return getusers()
@app.route('/addpoints/<int:id>&<int:c>', methods=['PUT'])
def addpoints(id,c):
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="12345",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="PointShop")
    cursor = connection.cursor()
    print(c)
    update_query = f"""UPDATE public.users SET points = points+{c} WHERE "id" = {id}"""
    cursor.execute(update_query)
    connection.commit()
    return getusers()
@app.route('/deleteitem/<int:id>', methods=['DELETE'])
def deleteitem(id):
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="12345",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="PointShop")
    cur = connection.cursor()
    sql_query =f"""DELETE FROM public."Items" WHERE "Id" = {id} """
    cur.execute(sql_query)
    print(sql_query)
    connection.commit()
    return getitems()
@app.route('/deleteuser/<int:id>', methods=['DELETE'])
def deleteuser(id):
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="12345",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="PointShop")
    cur = connection.cursor()
    sql_query =f"""DELETE FROM public."users" WHERE "id" = {id} """
    out = cur.execute(sql_query)
    print(sql_query)
    connection.commit()
    return getusers()
@app.route('/adduser/<int:tgID>&<int:points>&<string:fio>', methods=['POST'])
def adduser(tgID,points,fio):
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="12345",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="PointShop")
    cur = connection.cursor()
    sql_query =f"""INSERT INTO public."users" ("telegramID", "points", "fio") VALUES ({tgID},{points},'{fio}') """
    out = cur.execute(sql_query)
    connection.commit()
    return getusers()
@app.route('/additem/<string:name>&<int:price>&<int:count>', methods=['POST'])
def additem(name,price,count):
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="12345",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="PointShop")
    cur = connection.cursor()
    sql_query =f"""INSERT INTO public."Items" ("Name", "Price", "Count") VALUES ('{name}',{price},{count}) """
    out = cur.execute(sql_query)
    connection.commit()
    return getitems()
@app.route('/getitems', methods=['GET'])
def getitems():
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="12345",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="PointShop")
    cur = connection.cursor()
    sql_query ="""SELECT json_agg(t)
from (SELECT * FROM public."Items") t """
    out = cur.execute(sql_query)
    print(sql_query)
    context_records = cur.fetchall()
    ContextRootKeys = []
    for row in context_records:
        ContextRootKeys.append(row)
    connection.commit()
    print(ContextRootKeys)
    return jsonify(ContextRootKeys)
@app.route('/getitems/<int:id>', methods=['GET'])
def getitem(id):
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="12345",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="PointShop")
    cur = connection.cursor()
    sql_query =f"""SELECT json_agg(t)
from (SELECT * FROM public."Items" WHERE "Id" = {id}) t """
    out = cur.execute(sql_query)
    print(sql_query)
    context_records = cur.fetchall()
    ContextRootKeys = []
    for row in context_records:
        ContextRootKeys.append(row)
    connection.commit()
    print(ContextRootKeys)
    return jsonify(ContextRootKeys)
@app.route('/getusers', methods=['GET'])
def getusers():
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="12345",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="PointShop")
    cur = connection.cursor()
    sql_query ="""SELECT json_agg(t)
from (SELECT * FROM public."users") t """
    out = cur.execute(sql_query)
    print(sql_query)
    context_records = cur.fetchall()
    ContextRootKeys = []
    for row in context_records:
        ContextRootKeys.append(row)
    connection.commit()
    print(ContextRootKeys)
    return jsonify(ContextRootKeys)
@app.route('/getusers/<int:id>', methods=['GET'])
def getuser(id):
    connection = psycopg2.connect(user="postgres",

                                  password="12345",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="PointShop")
    cur = connection.cursor()
    sql_query =f"""SELECT json_agg(t)
from (SELECT * FROM public."users" WHERE "id" = {id}) t """
    out = cur.execute(sql_query)
    print(sql_query)
    context_records = cur.fetchall()
    ContextRootKeys = []
    for row in context_records:
        ContextRootKeys.append(row)
    connection.commit()
    print(ContextRootKeys)
    return jsonify(ContextRootKeys)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="62.113.109.225")