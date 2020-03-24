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
            self.visited.append(city)
        return self.visited

    def increasing(self):
        self.visited = self.cities
        return self.visited

    def cost(self):
        self.costs = 0.0
        i = 0
        for i in range(len(self.visited)-1):
            self.costs += calculation.distance(self.visited[i], self.visited[i+1])
        return self.costs

    def nearestNeighbor(self, city):
        res = float('inf')
        for nextCity in self.cities:
             if nextCity not in self.visited and calculation.distance(city,nextCity) < res:
                 res = calculation.distance(city, nextCity)
                 neighbor = nextCity
        return neighbor

    def searchNear(self):
        city = self.cities[0]
        self.visited.append(city)
        while len(self.visited) < len(self.cities):
            nextCity = self.nearestNeighbor(city)
            self.visited.append(city)
            city = nextCity
        return self.visited
