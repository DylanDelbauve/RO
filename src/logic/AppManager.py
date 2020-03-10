import src.logic.City as city
class AppManager:

    def __init__(self):
        self.window = None
        self.file = None
        self.cities = []

    def setfile(self,file):
        self.file = file
        self.readFile()
    
    def setWindow(self,window):
        self.window = window

    def readFile(self):
        data = self.file.readlines()
        for line in data:
            fields = line.split(" ")
            self.cities.append(city.City(fields[0], fields[1], fields[2]))