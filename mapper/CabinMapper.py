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

def getCabin():
    sql = "select * from cabin;"
    cursor.execute(sql)
    return cursor.fetchall()

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