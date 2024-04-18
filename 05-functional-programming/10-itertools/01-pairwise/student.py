from itertools import pairwise

def total_distance(path,distance):
    return sum([distance(city1,city2) for city1, city2 in list(pairwise(path))])