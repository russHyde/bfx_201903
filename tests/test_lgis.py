from rosa.testable import lgis

def test_it_isnt_greedy():
    assert lgis([1, 4, 2, 3, 5]) != [1, 4, 5]

def test_increasing_sequence():
    assert lgis([1, 3, 4, 2, 5, 7, 4]) == [1, 3, 4, 5, 7]
