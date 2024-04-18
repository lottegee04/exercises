def group_by(xs, key_function):
    return {key: [value for value in xs if key == key_function(value)] for key in {key_function(x) for x in xs}}