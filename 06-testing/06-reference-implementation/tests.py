import pytest
from student import Student
from search import binary_search, linear_search



@pytest.mark.parametrize("students,target_id",[
    ([],1),
    ([Student(x*2) for x in range(20)],50),
    ([Student(x) for x in range(100)],66), #
    ([Student(x) for x in range(100)],35), #   
    ([Student(x) for x in range(100)],0),
    ([Student(x) for x in range(50)],49), 
    ([Student(x) for x in range(55)],15) #
    
])

def test_binary_search(students,target_id):
    assert binary_search(students, target_id) == linear_search(students,target_id)