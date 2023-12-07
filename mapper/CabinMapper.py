from entity.Cabin import Cabin
from entity.Flight import Flight
from mapper.dbUtil import dbUtil

dbUtil = dbUtil()
conn = dbUtil.getConnect()
cursor = dbUtil.getCursor()

def addCabin(fid, flightDate, grade, seats, availableSeats, fullPrice):
    sql = "insert into cabin (fid, flightDate, grade, seats, availableSeats, fullPrice) values (%s, %s, %s, %s, %s, %s);"
    curs = conn.cursor()
    curs.execute(sql, (fid, flightDate, grade, seats, availableSeats, fullPrice))
    conn.commit()
    curs.close()

def getCabin(flightNumber, fromCity, toCity, grade):
    sql = "select * from cabin inner join flight f on cabin.fid = f.fid where 1"
    params = list()
    if flightNumber != None:
        sql += " and f.flightNumber like CONCAT('%%', %s, '%%')"
        params.append(flightNumber)
    if fromCity != None:
        sql += " and f.fromCity like CONCAT('%%', %s, '%%')"
        params.append(fromCity)
    if toCity != None:
        sql += " and f.toCity like CONCAT('%%', %s, '%%')"
        params.append(toCity)
    if grade != None:
        sql += " and grade = %s"
        params.append(grade)
    sql += ";"
    cursor.execute(sql, params)
    resultSet = cursor.fetchall()
    cabinList = list()
    if len(resultSet) > 0:
        for resultMap in resultSet:
            flight = Flight(resultMap["fid"], resultMap["flightNumber"], resultMap["model"], resultMap["fromCity"], resultMap["toCity"], resultMap["mileAge"], resultMap["departureTime"])
            cabinList.append(Cabin(resultMap["cid"], flight, resultMap["flightDate"], resultMap["grade"], resultMap["seats"], resultMap["availableSeats"], resultMap["fullPrice"]))
        return cabinList
    return None

def updataCabinByCid(cid, fid, flightDate, grade, seats, availableSeats, fullPrice):
    sql = "update cabin set "
    params = list()
    if fid != None:
        sql += "fid = %s, "
        params.append(fid)
    if flightDate != None:
        sql += "flightDate = %s, "
        params.append(flightDate)
    if grade != None:
        sql += "grade = %s, "
        params.append(grade)
    if seats != None:
        sql += "seats = %s, "
        params.append(seats)
    if availableSeats != None:
        sql += "availableSeats = %s, "
        params.append(availableSeats)
    if fullPrice != None:
        sql += "fullPrice = %s, "
        params.append(fullPrice)
    sql = sql[:len(sql) - 2]
    sql += " where cid = %s"
    params.append(cid)

    curs = conn.cursor()
    curs.execute(sql, params)
    conn.commit()
    curs.close()

def deleteCabinByCid(cid):
    sql = "delete from cabin where cid = %s;"
    curs = conn.cursor()
    curs.execute(sql, (cid))
    conn.commit()
    curs.close()

def allClose():
    cursor.close()
    conn.close()