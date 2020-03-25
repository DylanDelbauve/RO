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

    def cost(self):
        return self.lastAlgo.cost(self.lastAlgo.visited())

    def result(self,algorithm):
        self.lastAlgo = algo.Algo(self.cities)
        res = None
        if algorithm == 0:
            res = self.lastAlgo.random()
        elif algorithm == 1:
            res = self.lastAlgo.increasing()
        elif algorithm == 2:
            res = self.lastAlgo.searchNear()
        elif algorithm == 3:
            res = self.lastAlgo.localSearch()
        return res

    def __str__(self):
        temp = []
        for city in self.lastAlgo.visited:
            temp.append(city.id)
        return temp
