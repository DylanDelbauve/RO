import src.logic.City as city
import src.logic.Algo as algo
class AppManager:

    def __init__(self):
        self.window = None
        self.cities = []

    
    def setWindow(self,window):
        self.window = window

    def readFile(self,file):
        data = file.readlines()
        for line in data:
            fields = line.split(" ")
            self.cities.append(city.City(fields[0], fields[1], fields[2]))
        return self.cities

    def random(self):
        rand = algo.Algo(self.cities)
        return rand.random()
    
    def increasing(self):
        inc = algo.Algo(self.cities)
        return inc.increasing()