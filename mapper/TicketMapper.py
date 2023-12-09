import time

from entity.Cabin import Cabin
from entity.Flight import Flight
from entity.Ticket import Ticket
from mapper.dbUtil import dbUtil

dbUtil = dbUtil()
conn = dbUtil.getConnect()
cursor = dbUtil.getCursor()

def addTicket(uid, fid, cid, isPayment):
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
        sql += " and f.fromCity like CONCAT('%%', %s, '%%')"
        params.append(fromCity)
    if toCity != None:
        sql += " and f.toCity like CONCAT('%%', %s, '%%')"
        params.append(toCity)
    sql += ";"

    cursor.execute(sql, params)
    resultSet = cursor.fetchall()
    ticketList = list()
    if len(resultSet) >0:
        for resultMap in resultSet:
            flight = Flight(resultMap["fid"], resultMap["flightNumber"], resultMap["model"], resultMap["fromCity"], resultMap["toCity"], resultMap["mileAge"], resultMap["departureTime"])
            cabin = Cabin(resultMap["cid"], flight, resultMap["flightDate"], resultMap["grade"], resultMap["seats"], resultMap["availableSeats"], resultMap["fullPrice"])
            ticketList.append(Ticket(resultMap["tid"], resultMap["uid"], cabin, resultMap["bayTime"], resultMap["isPayment"]))
        return ticketList
    return None

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