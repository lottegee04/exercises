def indices_of(xs,condition):
    ls =[]
    for x in range(len(xs)):
        if condition(xs[x]):
            ls.append(x)
    return ls