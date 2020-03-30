class Station:
    def __init__(self, id, stationName, t):
        self.id = id
        self.stationName = stationName
        self.t = t

class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.checkout = {}
        self.ls = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        s = Station(id, stationName, t)
        self.checkin[id] = s

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        ci = self.checkin[id]
        s = ci.stationName + '-' + stationName
        if s not in self.ls:
            self.ls[s] = [t - ci.t]
        else:
            self.ls[s].append(t - ci.t)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        s = startStation + '-' + endStation
        if s not in self.ls:
            return 0
        return sum(self.ls[s]) / len(self.ls[s])

undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkIn(32, "Paradise", 8)
undergroundSystem.checkIn(27, "Leyton", 10)
undergroundSystem.checkOut(45, "Waterloo", 15)
undergroundSystem.checkOut(27, "Waterloo", 20)
undergroundSystem.checkOut(32, "Cambridge", 22)
print(undergroundSystem.getAverageTime("Paradise", "Cambridge"))
undergroundSystem.getAverageTime("Leyton", "Waterloo")
undergroundSystem.checkIn(10, "Leyton", 24)
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))
undergroundSystem.checkOut(10, "Waterloo", 38)
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))