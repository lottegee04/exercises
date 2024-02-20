# Write your code here
def odd_keys_dict(dictionary):
    result = dictionary.copy()
    for i in dictionary.keys():
        if i % 2 == 0:
            del result[i]
    return result