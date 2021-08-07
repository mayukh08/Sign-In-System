import sqlite3
from hashlib import blake2b


def insert_user():
    conn = sqlite3.connect('signin.db')
    cursor = conn.cursor()

    sql = ''' CREATE TABLE USER (username text, email text, hashed_password text)'''
    cursor.execute(sql)

    hlib = blake2b(key=b'signin12343434')
    hlib.update('abcdef'.encode('utf-8'))
    hash_passcode = hlib.hexdigest()

    sql1 = f''' INSERT INTO USER VALUES ("Mayukh","mayukh2014story@gmail.com", "{hash_passcode}") '''
    cursor.execute(sql1)
    conn.commit()

    sql2 = "SELECT * FROM USER"
    cursor.execute(sql2)
    all_items = cursor.fetchall()

    print(all_items)

    conn.close()


insert_user()