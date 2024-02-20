# Write your code here
def digit_sum(n):
    count =0
    string = str(n)

    for i in string:
        j = int(i)
        count+=j
    string = str(count)
    return int(string)

def last_digit(n):
    return n%10

def remove_last_digit(n):
    return n//10
