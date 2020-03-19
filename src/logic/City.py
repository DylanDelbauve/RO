class City:
    def __init__(self, id, lon, lat):
        self.id = id
        self.lon = float(lon)
        self.lat = float(lat)

    def str(self):
        return str(self.id)+" "+str(self.lon)+" "+str(self.lat)

    def long(self):
        return self.lon

    def lat(self):
        return self.lat
