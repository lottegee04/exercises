import sys
sys.path.append("..")
def title_to_director(movies):
    return {movie.title:movie.director for movie in movies}

def director_to_titles(movies):
    directors = {movie.director for movie in movies}
    
    return {}