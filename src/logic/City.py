class City:
    def __init__(self, name, long, lat):
        self.name = name
        self.long = long
        self.lat = lat

    def __str__(self):
        return self.name+" "+str(self.long)+" "+str(self.lat) 
