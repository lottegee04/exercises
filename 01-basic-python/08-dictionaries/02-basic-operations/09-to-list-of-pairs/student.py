# Write your code here
def to_list_of_pairs(dictionary):
    list = []
    for i in dictionary.keys():
        list.append((i,dictionary[i]))
    return list