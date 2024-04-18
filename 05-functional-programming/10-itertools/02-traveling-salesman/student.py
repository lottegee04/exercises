from itertools import pairwise
from itertools import permutations


def find_shortest_path(distance,city_count):
    def total_distance(path):
        return sum([distance(city1,city2) for city1, city2 in pairwise(path)])
    paths = ([0,*p,0] for p in permutations(range(1,city_count)))
    return min(paths, key=total_distance)
    
#met solutions gemaakt