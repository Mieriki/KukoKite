import mapper.FlightMapper as flightMapper

#添加航线
def addFlight(flightNumber, model, fromCity, toCity, mileAge, departureTime):
    return flightMapper.addFlight(flightNumber ,model ,fromCity, toCity, mileAge, departureTime)

#获取所有航线
def getFlight(flightNumber, fromCity, toCity):
    return flightMapper.getFlight(flightNumber, fromCity, toCity)

#更改航线信息
def updataFlight(fid, flightNumber, model, fromCity, toCity, mileAge, departureTime):
    return flightMapper.updataFightByFid(fid, flightNumber ,model, fromCity, toCity, mileAge, departureTime)

#删除航线
def deleteFlight(fid):
    return flightMapper.deleteFlightByFid(fid)
