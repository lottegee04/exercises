import pytest
from mystatistics import average

@pytest.mark.parametrize('ns,expected',[
    ([2,4,6],4),
    ([0.1,0.1,0.1],0.1),
    ([25,75], 50)
])
def test_average(ns,expected):
    assert average(ns) == pytest.approx(expected,abs=0.01)