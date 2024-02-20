# Write your code here
def double_dict_values(dictionary):
    new_dict ={}
    for key,value in dictionary.items():
        new_dict[key] = value*2
    return new_dict