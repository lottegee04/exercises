def cycle(xs):
    current = 0
    while True:
        yield xs[current]
        current+=1
        if current == len(xs):
            current = 0


def alt_cycle(values):
    # If values is an iterator, we need to make a copy
    values = list(values)
    while True:
        for value in values:
            yield value


def alternative_cycle(values):
    values = list(values)
    while True:
        yield from values  # "yield from xs" yields each element in xs in turn
