class UndergroundSystem:

    def __init__(self):
        self.M = {} #map id to its start time and station name
        self.event = defaultdict(lambda: [0, 0]) #map (startStation, endStation) to  total time and total number of trips, this way ensures O(1) for getaveragetime, otherwise, we need to computer mean each time, which is O(n)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.M[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        #find the correspoinding id, start time and start stationName
        startStation, startTime = self.M.pop(id)
        self.event[(startStation, stationName)][0] += t - startTime
        self.event[(startStation, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.event[(startStation, endStation)][0]/self.event[(startStation, endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)