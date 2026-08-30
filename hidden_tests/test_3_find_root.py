from q3_find_root import find_root 


def test_find_root():
    import math # we use math.isclose to compare floats
    
    assert(math.isclose(find_root(1, -7, 10), 5))
    assert(math.isclose(find_root(1, 0, -9), 3))
    assert(math.isclose(find_root(10, -29, -21), 3.5))
    assert(math.isclose(find_root(1, -2, 1), 1))
    