def findMaximum(list):
    
    if len(list) == 1:
        return list[0]
    
    if list[0] > list[1]:
        list.remove(list[1])
        return findMaximum(list)
    else:
        return findMaximum(list[1:])