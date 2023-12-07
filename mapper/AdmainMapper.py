import pymysql

from entity.Admin import Admin

conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd='Inaba', db='Kuko', charset='utf8mb4')
cursor = conn.cursor(pymysql.cursors.DictCursor)

def addAdmin(userName, password, permissionLevel):
    sql = "insert into admin (userName, password, permissionLevel) values (%s, %s, %s);"
    curs = conn.cursor()
    curs.execute(sql, (userName, password, permissionLevel))
    conn.commit()
    curs.close()

def getAdminByUserNameAndPassword(userName, password):
    sql = "select * from admin where userName = %s and password = %s;"
    cursor.execute(sql, (userName, password))
    resultSet = cursor.fetchall()
    if len(resultSet) > 0:
        resultMap = resultSet[0]
        return Admin(resultMap["aid"], resultMap["userName"], resultMap["password"], resultMap["permissionLevel"])
    return None


def updataAdminByAid(aid, userName, password, permissionLevel):
    sql = "update admin set "
    params = list()
    if userName != None:
        sql += "userName = %s, "
        params.append(userName)
    if password != None:
        sql += "password = %s, "
        params.append(password)
    if permissionLevel != None:
        sql += "permissionLevel = %s, "
        params.append(permissionLevel)
    sql = sql[:len(sql) - 2]
    sql += " where aid = %s"
    params.append(aid)

    curs = conn.cursor()
    curs.execute(sql, params)
    conn.commit()
    curs.close()

def deleteAdminByAid(aid):
    sql = "delete from admin where aid = %s;"
    curs = conn.cursor()
    print(curs.execute(sql, (aid)))
    conn.commit()
    curs.close()

def allClose():
    cursor.close()
    conn.close()