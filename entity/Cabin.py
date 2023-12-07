from entity.Flight import Flight

class Cabin:
    def __init__(self, cid, flight, flightDate, grade, seats, availableSeats, fullPrice):
        self.cid = cid
        self.flight = flight
        self.flightDate = flightDate
        self.grade = grade
        self.seats = seats
        self.availableSeats = availableSeats
        self.fullPrice = fullPrice