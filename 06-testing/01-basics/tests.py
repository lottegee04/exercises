from intervals import overlapping_intervals


def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert not overlapping_intervals((2, 5), (7, 10))
    #mijn cases
    assert overlapping_intervals((-5,10), (9,11))
    assert not overlapping_intervals((0,4),(4,0))
    assert not overlapping_intervals((-5,-7),(-6,-2))
    assert overlapping_intervals((-20,-15),(-16,1))
    #cases i found via the verify
    assert overlapping_intervals((0,0),(0,0))
    assert overlapping_intervals((1,1),(0,2))