import pymysql
import time

from entity.User import User

conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd='Inaba', db='Kuko', charset='utf8mb4')
cursor = conn.cursor(pymysql.cursors.DictCursor)

def addUser(userName, password, phone):
    sql = "insert into user (userName, password, phone, creationDate) values (%s, %s ,%s, %s);"
    tame = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    curs = conn.cursor()
    curs.execute(sql,(userName, password, phone, tame))
    conn.commit()
    curs.close()

def updataUserByUid(uid, userName, password, phone):
    sql = "update user set "
    params = list()
    if userName != None:
        sql += "userName = %s, "
        params.append(userName)
    if password != None:
        sql += "password = %s, "
        params.append(password)
    if phone != None:
        sql += "phone = %s, "
        params.append(phone)
    sql = sql[:len(sql) - 2]
    sql += " where uid = %s"
    params.append(uid)

    curs = conn.cursor()
    curs.execute(sql, params)
    conn.commit()
    curs.close()

def getUserByUserNameAndPassword(userName, password):
    sql = "select * from user where userName = %s and password = %s;"
    cursor.execute(sql, (userName, password))
    resultSet = cursor.fetchall()
    if len(resultSet) > 0:
        resultMap = resultSet[0]
        return User(resultMap["uid"], resultMap["userName"], resultMap["password"], resultMap["phone"], resultMap["creationDate"])
    return None

def deleteUserByUid(uid):
    sql = "delete from user where uid = %s;"
    curs = conn.cursor()
    curs.execute(sql, (uid))
    conn.commit()
    curs.close()

def allClose():
    cursor.close()
    conn.close()