# Write your code here
def  drop_nth(xs, n):
    list = xs.copy()
    del list[n]
    return list

drop_nth(['b', 'c', 'd', 'e'],0)
print(drop_nth(['b', 'c', 'd', 'e'],0))