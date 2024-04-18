def merge_dictionaries(d1,d2,merge_function):
    return_dict = {}
    for key1,value1 in d1.items():
        if key1 in d2.keys():
            return_dict[key1] = merge_function(d1[key1], d2[key1])
        else:
            return_dict[key1] = value1
    for key2,value2 in d2.items():
        if key2 not in d1.keys():
            return_dict[key2]=value2
    return return_dict