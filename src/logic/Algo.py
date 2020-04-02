import random as rnd
from math import sqrt


def distance(src, dest):
    """ Calcule la distance entre 2 villes

    :param src:
    :param dest:
    :return:
    """
    temp = sqrt((dest.lon - src.lon) ** 2 + (dest.lat - src.lat) ** 2) * 100
    return temp


class Algo:

    def __init__(self, cities):
        self.visited = list()
        self.cities = cities
        self.costs = 0.0

    def random(self):
        """ Algo d'une tournée aléatoire

        :return: la tournée aléatoire
        """
        temp = self.cities
        rnd.shuffle(temp)
        for city in temp:
            self.visited.append(city)
        return self.visited

    def increasing(self):
        """ Algo de tournée croissante

        :return: la tournée croissante
        """
        self.visited = self.cities
        return self.visited

    def cost(self, tour):
        """ Calcule la distance totale de la tournée

        :param tour: la tournée
        :return: la distance totale
        """
        self.costs = 0.0
        i = 0
        for i in range(len(tour) - 1):
            self.costs += distance(tour[i], tour[i + 1])
        self.costs += distance(tour[65], tour[0])
        return self.costs

    def nearest_neighbor(self, city):
        """ Recherche la ville voisin la plus proche

        :param city: Ville dont on veut trouver le voisin
        :return: le voisin le plus procher
        """
        temp = float("inf")
        for nextCity in self.cities:
            if nextCity not in self.visited and distance(city, nextCity) < temp:
                temp = distance(city, nextCity)
                neighbor = nextCity
        return neighbor

    def search_near(self):
        """ Algo de recherche du plus proche voisin

        :return: une tournée du plus proche voisin
        """
        city = self.cities[0]
        self.visited.append(city)
        while len(self.visited) < len(self.cities):
            next_city = self.nearest_neighbor(city)
            self.visited.append(next_city)
            city = next_city
        return self.visited

    def local_search(self):
        """ Algo de recherche locale

        :return: une tournée de recherche locale
        """
        self.search_near()
        res = self.visited
        if self.cost(res) > self.cost(self.exchange_near(res)):
            res = self.exchange_near(res)
        if self.cost(res) > self.cost(self.exchange_random(res)):
            res = self.exchange_random(res)
        return self.visited

    def exchange_near(self, tour):
        """ Teste les voisins d'une tournée par échange de 2 sommets consécutifs

        :param tour: la tournée à tester
        :return: la nouvelle tournée
        """
        res = []
        temp = []
        res = self.visited
        temp = self.visited

        for i in range(len(self.visited) - 1):
            temp[i], temp[i+1] = temp[i+1], temp[i]
            if self.cost(res) > self.cost(temp):
                res = temp
            else:
                temp = res

        return res

    def exchange_random(self, tour):
        """ Teste les voisins d'une tournée par échange de 2 sommets aléatoires

        :param tour: la tournée à tester
        :return: la nouvelle tournée
        """
        res = []
        temp = []
        res = self.visited
        temp = self.visited

        for i in range(len(self.visited) - 1):
            city = temp[i]
            exit = False
            for j in range(len(self.visited) - 1):
                if not exit:
                    temp[i], temp[j] = temp[j], temp[i]
                    if self.cost(res) > self.cost(temp):
                        res = temp
                        exit = True
                    else:
                        temp = res
        return res