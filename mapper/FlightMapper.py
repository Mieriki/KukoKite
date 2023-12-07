from entity.Flight import Flight
from mapper.dbUtil import dbUtil

dbUtil = dbUtil()
conn = dbUtil.getConnect()
cursor = dbUtil.getCursor()

def getFlight(flightNumber, fromCity, toCity):
    sql = "select * from flight where 1 "
    params = list()
    if flightNumber != None:
        sql += " and flightNumber like CONCAT('%%', %s, '%%')"
        params.append(flightNumber)
    if fromCity != None:
        sql += " and fromCity like CONCAT('%%', %s, '%%')"
        params.append(fromCity)
    if toCity != None:
        sql += " and toCity like CONCAT('%%', %s, '%%')"
        params.append(toCity)
    cursor.execute(sql, params)
    sql += ";"
    resultSet = cursor.fetchall()
    if len(resultSet) > 0:
        flightList = list()
        for flight in resultSet:
            flightList.append(Flight(flight["fid"], flight["flightNumber"], flight["model"], flight["fromCity"], flight["toCity"], flight["mileAge"], flight["departureTime"]))
        return flightList
    return None

def addFlight(flightNumber, model, fromCity, toCity, mileAge, departureTime):
    sql = "insert into flight (flightNumber, model, fromCity, toCity, mileAge, departureTime) values (%s, %s, %s, %s, %s, %s);"
    curs = conn.cursor()
    curs.execute(sql,(flightNumber, model, fromCity, toCity, mileAge, departureTime))
    conn.commit()
    curs.close()

def deleteFlightByFid(fid):
    sql = "delete from flight where fid = %s;"
    curs = conn.cursor()
    curs.execute(sql, (fid))
    conn.commit()
    curs.close()

def updataFightByFid(fid, flightNumber, model, fromCity, toCity, mileAge, departureTime):
    sql = "update flight set "
    params = list()
    if flightNumber != None:
        sql += "flightNumber = %s, "
        params.append(flightNumber)
    if model != None:
        sql += "model = %s, "
        params.append(model)
    if fromCity != None:
        sql += "fromCity = %s, "
        params.append(fromCity)
    if toCity != None:
        sql += "toCity = %s, "
        params.append(toCity)
    if mileAge != None:
        sql += "mileAge = %s, "
        params.append(mileAge)
    if departureTime != None:
        sql += "departureTime = %s, "
        params.append(departureTime)
    sql = sql[:len(sql) - 2]
    sql += " where fid = %s"
    params.append(fid)

    curs = conn.cursor()
    curs.execute(sql, params)
    conn.commit()
    curs.close()

def allClose():
    cursor.close()
    conn.close()