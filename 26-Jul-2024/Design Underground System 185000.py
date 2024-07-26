# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__ (self):
        self.timeTaken = {}
        self.start = {}
    
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start = self.start[id][0]
        dif = t - self.start[id][1]
        if (start,stationName) in self.timeTaken:
            av = self.timeTaken[(start,stationName)][0]
            num = self.timeTaken[(start,stationName)][1] +1
            average = ((av * (num-1)) + dif)/num
            self.timeTaken[(start,stationName)] = [average,num]
        else:
            self.timeTaken[(start,stationName)] = [dif,1]
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.timeTaken[(startStation,endStation)][0]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)