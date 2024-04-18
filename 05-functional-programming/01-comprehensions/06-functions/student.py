import re

def movie_count(movies,director):
    return len([movie for movie in movies if movie.director == director])

def longest_movie_runtime_with_actor(movies, actor):
    return max([movie.runtime for movie in movies if actor in movie.actors])

def has_director_made_genre(movies, director, genre):
    return len([movie for movie in movies if movie.director == director and genre in movie.genres]) != 0

def is_prime(n):
    return len([x for x in range(2,n) if n%x==0]) == 0 and n >= 2

def is_increasing(ns):
    return len([x for x in range(len(ns)-1) if ns[x] > ns[x+1] ]) == 0

def count_matching(xs,ys):
    return len([x for x in range(min([len(xs),len(ys)])) if xs[x] == ys[x]])

def weighted_sum(ns, weight):
    return sum([ns[x] * weight[x] for x in range(min([len(ns),len(weight)]))])

def alternating_caps(string):
    chars = [char.upper() if index %2 == 0 else char.lower() for index,char in enumerate(string)]
    return "".join(chars)

def find_repeated_words(sentence):
    import re
    words = [ word.lower() for word in re.findall(r'[a-zA-Z]+',sentence)]
    return {word1 for word1, word2 in zip(words, words[1:]) if word1 == word2}

sentence = 'this Sentence has Has repeated words. Words'
print(is_increasing([1, 2, 3, 3, 4, 5, 6]))