import mapper.CabinMapper as cabinMapper

#获取舱位
def getCabin(flightNumber, fromCity, toCity, grade):
    return cabinMapper.getCabin(flightNumber, fromCity, toCity, grade)

#更改舱位
def updataCabin(cid, fid, flightDate, grade, seats, availableSeats, fullPrice):
    return cabinMapper.updataCabinByCid(cid, fid, flightDate, grade, seats, availableSeats, fullPrice)

#添加舱位
def addCabin(fid, flightDate, grade, seats, availableSeats, fullPrice):
    return cabinMapper.addCabin(fid, flightDate, grade, seats, availableSeats, fullPrice)

#删除舱位
def deleteCabin(cid):
    return cabinMapper.deleteCabinByCid(cid)