import collections

class UndergroundSystem:
    # when someone checks out, we want to make sure we are NOT accounting for them when we get the getAverageTime
    # when someone checks out, they can also check in at another station as if they are brand new 
    # testing the findAverageTime function => [a, b], [b, a] to make sure we are not messing up from point a to point base_exec_prefix
    # making sure the logic is correct for finding the average

    def __init__(self):
        self.start_hash = {}
        self.start_times = {}
        self.route_times = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start_hash[id] = stationName
        self.start_times[id] = t

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.route_times[f"{self.start_hash[id]}->{stationName}"].append(t - self.start_times[id])
        self.start_hash.pop(id)
        self.start_times.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.route_times[f"{startStation}->{endStation}"]
        return sum(times) / len(times)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
