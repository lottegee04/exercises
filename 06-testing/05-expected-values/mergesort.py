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
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

def merge_sort(ns):
    if len(ns)==0 or len(ns) ==1:
        return ns
    left,right = split_in_two(ns)
    sorted_left = merge_sort(left)
    sorted_right =merge_sort(right)
    
    return merge_sorted(sorted_left,sorted_right)
print(split_in_two([4, 6, 78, 100, 99]))
print(merge_sort([4, 6, 78, 100, 99]))

[4, 6, 78, 100, 99]
[4, 6, 99, 78, 100]
[4, 6, 99, 100, 78]
[4, 6, 100, 78, 99]
[4, 6, 100, 99, 78]