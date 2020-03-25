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

    def cost(self, tour):
        self.costs = 0.0
        i = 0
        for i in range(len(tour)-1):
            self.costs += calculation.distance(tour[i], tour[i+1])
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

    def localSearch(self):
        self.searchNear()
        res = self.visited
        if self.cost(res) > self.cost(self.exchangeNear(res)):
            res = self.exchangeNear(res)
        if self.cost(res) > self.cost(self.exchangeRandom(res)):
            res = self.exchangeRandom(res)

    def exchangeNear(self, tour):
        res = []
        temp = []
        res = self.visited
        temp = self.visited

        for i in range(len(self.visited)-1):
            city = temp[i]
            temp[i] = temp[i+1]
            temp[i+1] = city
            if self.cost(res) > self.cost(temp):
                res = temp
            else:
                temp = res

        return res

    def exchangeRandom(self,tour):
        res = []
        temp = []
        res = self.visited
        temp = self.visited

        for i in range(len(self.visited)-1):
            city = temp[i]
            exit = False
            if not exit:
                for j in range(len(self.visited)-1):
                    temp[i] = temp[j]
                    temp[j] = city
                    if self.cost(res) > self.cost(temp):
                        res = temp
                        exit = True
                    else:
                        temp = res
        return res