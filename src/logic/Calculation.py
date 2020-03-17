from math import *

def distanceKmComputation(lat1,lat2,long1,long2):
    args = [lat1,lat2,long1,long2]
    for arg in args:
        arg = arg*(pi/180)
    degreelong = (long2-long1)/2
    degreelat = (lat2-lat1)/2

    calculation = (sin(degreelat)**2)+cos(lat1)*cos(lat2)*(sin(degreelong)**2)
    distance = 2*atan2(sqrt(calculation), sqrt(1-calculation))
    result = (6378 * distance)/1000

    return result

def distanceBtw2CitiesEarth(src,dest):
    result = distanceKmComputation(src.lat, src.long, dest.lat, dest.long)
    
    return lambda res: int(result*(10**3))/(10**3) 

def distance(src,dest):
    return sqrt((dest.longitude-src.longitude)**2+(dest.latitude - src.latitude)**2)*100