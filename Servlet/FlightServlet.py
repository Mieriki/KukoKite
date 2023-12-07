import mapper.FlightMapper as flightMapper

#添加航线
def addFlight(flightNumber, model, fromCity, toCity, mileAge, departureTime):
    return flightMapper.addFlight(flightNumber ,model ,fromCity, toCity, mileAge, departureTime)

#获取所有航线
def getFlight():
    return flightMapper.getFlight()


print(getFlight())