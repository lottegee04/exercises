# Write your code here
def median(ns):
    ns_list = ns.copy()
    list = []
    while len(ns_list) != 0:
        list.append(min(ns_list))
        ns_list.remove(min(ns_list))
    if len(list) %2 != 0:
        return list[len(list)//2]
    else:
        return (list[(len(list)//2) -1] + list[len(list)//2]) /2
