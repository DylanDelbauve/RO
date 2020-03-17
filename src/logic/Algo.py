import random as rnd
import src.logic.Calculation as calculation

class Algo:

    def __init__(self, cities):
        self.visited = list()
        self.cities = cities
        self.costs = 0.0

    def random(self):
        temp = self.cities
        rnd.shuffle(temp)
        for city in temp:
            self.visited.append(city.name)
        return self.visited

    def increasing(self):
        temp = self.cities
        for city in temp:
            self.visited.append(city.name)
            nextCity = self.cities[+1]
            self.costs += calculation.distance(city,nextCity)
        return self.visited