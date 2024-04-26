def split_in_two(ns):
    return ([*ns[:len(ns)//2]], [*ns[len(ns)//2:]])

def merge_sorted(left,right):
    result =[]
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index+=1
        else:
            result.append(right[right_index])
            right_index+=1
    if left_index < len(left):
        result = [ *result, *left[left_index:]]
    
    if right_index < len(right):
        result = [*result ,*right[right_index:]]
    return result