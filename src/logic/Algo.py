import random as rnd

class Algo:

    def __init__(self, cities):
        self.visited = list()
        self.cities = cities
        self.costs = 0.00

    def random(self):
        self.visited = rnd.shuffle(self.cities)
        return self.visited