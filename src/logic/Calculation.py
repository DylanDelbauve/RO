from math import *

def distance(src, dest):
    temp = sqrt((dest.lon - src.lon) ** 2 + (dest.lat - src.lat) ** 2) * 100
    return temp