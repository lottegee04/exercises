# Write your code here
def is_increasing(ns):
    if len(ns) ==0:
        return True
    ms = ns.copy()
    ms.pop(0)
    ls = list(zip(ns,ms))
    for i,j in ls:
        if i>j:
            return False
    return True
    
ns = [1, 2, 3]