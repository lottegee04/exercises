def take_while(xs, condition):
    list1 = []
    list2 = []
    for x in xs:
        if condition(x):
            list1.append(x)
        else:
            list2 = xs.copy()[xs.index(x):]
            return (list1,list2)
            
    return (list1,list2)

def is_negative(x):
    return x < 0

print(take_while([-4, -2, 0, -1, 4, 6],is_negative))
