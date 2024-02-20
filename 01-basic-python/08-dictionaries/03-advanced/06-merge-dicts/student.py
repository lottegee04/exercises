# Write your code here
def merge_dicts(dict1, dict2):
    new_dict = {}
    for  key, value in dict1.items():
        new_dict[key] = value
    for key, value in dict2.items():
        new_dict[key] = value
    return new_dict