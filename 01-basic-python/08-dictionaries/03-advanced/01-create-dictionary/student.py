# Write your code here
def create_dictionary(keys, values):
    list_of_pairs =  list(zip(keys,values))
    diction = {}
    for key, value in list_of_pairs:
        diction[key] = value
    return diction