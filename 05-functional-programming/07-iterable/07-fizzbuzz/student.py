def fizzbuzz():
    current = 1
    while True:
        if current % 3 == 0 and current % 5 !=0:
            yield "fizz"
        elif current % 3 != 0 and current % 5 == 0:
            yield "buzz"
        elif current % 3 == 0 and current % 5 == 0:
            yield "fizzbuzz"
        else:
            yield str(current)
        current +=1                