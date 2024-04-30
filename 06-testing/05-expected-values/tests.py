import itertools
import pytest
from mergesort import merge_sort, merge_sorted, split_in_two
@pytest.mark.parametrize("ns",[
    ([value for value in range(length)]) for length in range(0,100)
])

def test_split_in_two(ns):
    test_data= split_in_two(ns)
    (left,right) = test_data
    
    assert [*left,*right] == ns
    assert len(test_data) == 2
    assert len(test_data) == pytest.approx(len(test_data),abs=1)

@pytest.mark.parametrize('left',[
    [],
    [1],
    [4,6],
    [1,2,3],
    [5,7,9,10,29],
    [2,5,8,9,10]
])
@pytest.mark.parametrize('right',[
    [],
    [2],
    [78,99,100],
    [5,6,7],
    [5,5,7,7,9],
    [4,9,10,14,18]
])
def test_merge_sorted(left,right):
    assert merge_sorted(left,right) == sorted(left+right)
    

@pytest.mark.parametrize('expected,ns',[
    (expected, list(permutation))
    for expected in [[],[1],[1,2,3],[4,9,12],[4,6,78,99,100]]
    for permutation in itertools.permutations(expected)
])
def test_merge_sort(expected,ns):
    assert merge_sort(ns) == expected