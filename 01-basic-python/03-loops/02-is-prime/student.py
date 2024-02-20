# Write your code here
def is_prime(n):
    i = 2
    if n == 0 or n == 1:
        return False
    while i<n:
        if n % i == 0:
            return False
        else:
            i+=1
    return True
is_prime(817)