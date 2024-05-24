from student import Student

def linear_search(students, target_id):
    for student in students:
        if student.id == target_id:
            return student
    return None

def binary_search(students, target_id):
    left,right = (0,len(students))
    
    for cycle in range(len(students)//2):
        middle = (left+right)//2
        if students[middle].id == target_id:
            return students[middle]
        elif students[middle].id > target_id:
            right = middle
        elif students[middle].id < target_id:
            left = middle
    return None
#helped with solution
#tip: doe eerst het meest logische (dus zonder -1 etc.) focus eerst op de niet grenzen
binary_search([Student(x) for x in range(100)],66)