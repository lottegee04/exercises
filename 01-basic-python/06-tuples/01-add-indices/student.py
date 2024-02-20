# Write your code here
def add_indices(xs):
    ns = []
    for i in range(len(xs)):
        ns.append(i)
    return list(zip(ns, xs))


xs = ["a","b","c"]
print(add_indices(xs))