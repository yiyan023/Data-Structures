class UndergroundSystem(object):

    def __init__(self):
        self.checkedIn = {}
        self.trips = {}

    def checkIn(self, id, stationName, t):
        self.checkedIn[id] = [stationName, t]

    def checkOut(self, id, stationName, t):
        station, time = self.checkedIn[id]
        del self.checkedIn[id]

        if (station, stationName) not in self.trips:
            self.trips[(station, stationName)] = [t - time, 1]
        
        else:
            self.trips[(station, stationName)][0] += (t - time)
            self.trips[(station, stationName)][1] += 1
        
    def getAverageTime(self, startStation, endStation):
        total, num = self.trips[(startStation, endStation)]
        return total / num
