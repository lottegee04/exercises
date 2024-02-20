# Write your code here
def keys_with_value(dictionary, value):
    list = []
    for key, val in dictionary.items():
        if val == value:
            list.append(key)
    return list