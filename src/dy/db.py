import sqlite3

conn = sqlite3.connect('E:\\Sqlite\\base\\dy.db')


def db_insert(uid, name, pNum, time):
    sql = "INSERT INTO zhubo (uid,name,pNum,time) VALUES ( " + str(uid) + ",'" + name + "'," + str(pNum) + ", " + str(
        time) + ");"
    conn.execute(sql)
    conn.commit()
