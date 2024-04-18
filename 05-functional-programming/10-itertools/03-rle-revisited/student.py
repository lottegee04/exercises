from itertools  import groupby
def rle_encode(data):
    return ((value,sum(1 for _ in group)) for value, group in groupby(data))
#opgelost met chatgpt

def rle_decode(data):
    return (x for x,y in data for _ in range(y) )
#opgelost met pytest