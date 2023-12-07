import time

from mapper.dbUtil import dbUtil

dbUtil = dbUtil()
conn = dbUtil.getConnect()
cursor = dbUtil.getCursor()

def addCabin(uid, fid, cid, isPayment):
    sql = "insert into ticket (uid, fid, cid, bayTime, isPayment) values (%s, %s, %s, %s, %s);"
    curs = conn.cursor()
    bayTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    curs.execute(sql, (uid, fid, cid, bayTime, isPayment))
    conn.commit()
    curs.close()

def getTicketByUid(uid, fid, cid, isPayment, fromCity, toCity):
    sql = "select * from ticket t inner join flight f on t.fid = f.fid inner join cabin c on t.cid = c.cid where uid = %s"
    params = list()
    params.append(uid)
    if fid != None:
        sql += " and t.fid = %s"
        params.append(fid)
    if cid != None:
        sql += " and t.cid = %s"
        params.append(cid)
    if isPayment != None:
        sql += " and t.isPayment = %s"
        params.append(isPayment)
    if fromCity != None:
        sql += " and f.fromCity = %s"
        params.append(fromCity)
    if toCity != None:
        sql += " and f.toCity = %s"
        params.append(toCity)
    sql += ";"

    cursor.execute(sql, params)
    return cursor.fetchall()

def deleteTicKetByTid(tid):
    sql = "delete from ticket where tid = %s;"
    curs = conn.cursor()
    curs.execute(sql, (tid))
    conn.commit()
    curs.close()

def updataTicKetByTid(tid):
    sql = "update ticket set isPayment = 2;"
    curs = conn.cursor()
    curs.execute(sql)
    conn.commit()
    curs.close()

def allClose():
    cursor.close()
    conn.close()