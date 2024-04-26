import pytest
from parentheses import matching_parentheses

@pytest.mark.parametrize('string',[
    ("()((())())()"),
    ("()()(())"),
    ("()((()))(())"),
    ("()()()()"),
    ("((((()))))"),
    ("()"),
    ("(()())"),
    (""), #subjective:  should this return true or not?
])
def test_matching_parentheses(string):
    assert matching_parentheses(string), f"{string} should have matching parentheses"
    
@pytest.mark.parametrize('string',[
    (")()"),
    (")))((("), #here is a bug
    (")()("),# another bug
    (")()")
    
])

def test_nonmatching_parentheses(string):
    assert not matching_parentheses(string), f"{string} should not have matching parentheses"