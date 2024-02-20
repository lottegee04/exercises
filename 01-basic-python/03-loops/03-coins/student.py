# Write your code here
def coins(one, two, five, goal):
    for i in range(five+1):
        for j in range(two+1):
            for k in range(one+1):
                if (k)+ (j*2) +(i*5) == goal:
                    return True
    return False
        
