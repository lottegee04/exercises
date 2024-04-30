def linear_search(students, target_id):
    for student in students:
        if student.id == target_id:
            return student
    return None

def binary_search(students, target_id):
    left,right = (0,len(students)-1)
    middle = len(students)//2
    for cycle in range(len(students)//2):
        if students[middle] == target_id:
            return students[middle]
        elif middle > target_id:
            right = middle
            middle = right //2
        elif middle < target_id:
            left = middle
            middle = left + left//2
    return None