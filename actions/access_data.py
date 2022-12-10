import sqlite3
from line_chatbot_api import *


def data_connection(func):
    def warp(*args):
        global conn
        conn = sqlite3.connect('data.db')
        output = func(*args)
        if conn is not None:
            conn.close()

        return output
    return warp

@data_connection
def read_user_id(user_id):
    sql = f"SELECT `id` from `data` WHERE `id`='{user_id}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    if not data:
        user_name = line_bot_api.get_profile(user_id).display_name
        sql = f"INSERT INTO `data` (`id`, `name`) VALUES ('{user_id}', '{user_name}')"
        cursor.execute(sql)
        conn.commit()
        sql = f"SELECT `id` from `data` WHERE `id`='{user_id}'"
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
    return data[0]

@data_connection
def update_answer(user_id, answer):
    sql = f"UPDATE `data` set `answer`='{answer}' WHERE `id`='{user_id}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

@data_connection
def read_answer(user_id):
    sql = f"SELECT  `answer` from `data` WHERE `id`='{user_id}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    return data[0] if data else None

@data_connection
def update_key(user_id, key):
    sql = f"UPDATE `data` set `key`='{key}' WHERE `id`='{user_id}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

@data_connection
def read_key(user_id):
    sql = f"SELECT `key` from `data` WHERE `id`='{user_id}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    return data[0] if data else None

@data_connection
def read_hiragana(user_id):
    sql = f"SELECT `hiragana` from `data` WHERE `id`='{user_id}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    return eval(data[0]) if data else None

@data_connection
def update_hiragana(user_id, list):
    sql = f"UPDATE `data` set `hiragana`='{str(list)}' WHERE `id`='{user_id}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

@data_connection
def read_hiragana0(user_id):
    sql = f"SELECT `hiragana0` from `data` WHERE `id`='{user_id}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    return eval(data[0]) if data else None

@data_connection
def update_hiragana0(user_id, list):
    sql = f"UPDATE `data` set `hiragana0`='{str(list)}' WHERE `id`='{user_id}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

@data_connection
def read_katakana(user_id):
    sql = f"SELECT `katakana` from `data` WHERE `id`='{user_id}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    return eval(data[0]) if data else None

@data_connection
def update_katakana(user_id, list):
    sql = f"UPDATE `data` set `katakana`='{str(list)}' WHERE `id`='{user_id}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

@data_connection
def read_katakana0(user_id):
    sql = f"SELECT `katakana0` from `data` WHERE `id`='{user_id}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    return eval(data[0]) if data else None

@data_connection
def update_katakana0(user_id, list):
    sql = f"UPDATE `data` set `katakana0`='{str(list)}' WHERE `id`='{user_id}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()