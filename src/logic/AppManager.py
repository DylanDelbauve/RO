import src.logic.City as city
import src.logic.Algo as algo
class AppManager:

    def __init__(self):
        self.window = None
        self.cities = []
        self.lastAlgo = None

    
    def setWindow(self, window):
        self.window = window

    def readFile(self, file):
        data = file.readlines()
        for line in data:
            fields = line.split(" ")
            self.cities.append(city.City(int(fields[0]), float(fields[1]), float(fields[2])))
        return self.cities

    def random(self):
        self.lastAlgo = algo.Algo(self.cities)
        return self.lastAlgo.random()
    
    def increasing(self):
        self.lastAlgo = algo.Algo(self.cities)
        return self.lastAlgo.increasing()

    def searchNear(self):
        self.lastAlgo = algo.Algo(self.cities)
        return self.lastAlgo.searchNear()

    def cost(self):
        return self.lastAlgo.cost()
