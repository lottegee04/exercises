def rle_encode(data):
    data_iter = iter(data)
    count = 1
    try:
        previous = next(data_iter)
        
        for x in data_iter:
            if x  == previous:
                count+=1
            else:
                yield (previous,count)
                previous = x
                count = 1
        yield (previous, count)
    except StopIteration:
        pass
#!!!: x will initially be the second item of data, because data_iter has already yielded the first item to previous outside the loop.

def rle_decode(data):
    data_iter = iter(data)
    try:
        for char, count in data_iter:
            for x in range(count):
                yield char
    except StopIteration:
        pass