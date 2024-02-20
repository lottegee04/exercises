# Write your code here
def rotatte(xs,n):
    return [*xs[n:],*xs[:n]]

def rotate(xs,n):
    for i in range(n):
        x =xs.pop(0)
        xs.append(x)
        
