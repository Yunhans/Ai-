import sqlite3

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
def read_user_data(user_id):
    sql = f"SELECT `id` from `data` WHERE `id`='{user_id}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    if not data:
        sql = f"INSERT INTO `data` (`id`) VALUES ('{user_id}')"
        cursor.execute(sql)
        conn.commit()
        sql = f"SELECT `id` from `data` WHERE `id`='{user_id}'"
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
    return data

@data_connection
def update_answer(user_id, answer):
    sql = f"UPDATE `data` set `answer`='{answer}' WHERE `id`='{user_id}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

@data_connection
def read_answer(user_id):
    sql = f"SELECT `id`, `answer` from `data` WHERE `id`='{user_id}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    return data[1] if data else None