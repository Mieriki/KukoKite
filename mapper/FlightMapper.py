import pymysql

conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd='Inaba', db='Kuko', charset='utf8mb4')
cursor = conn.cursor(pymysql.cursors.DictCursor)

def getFlight():
    sql = "select * from flight;"
    cursor.execute(sql)
    return cursor.fetchall()

def addFight(flightNumber, model, fromCity, toCity, mileAge, departureTime):
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

deleteFlightByFid(6)