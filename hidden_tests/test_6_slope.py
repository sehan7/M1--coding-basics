from q6_slope import slope 


def test_slope():
    import math # we use math.isclose to compare floats
    assert(math.isclose(slope(1, 3, 6, 5), 0.4))
    assert(math.isclose(slope(2, 4, 6, 8), 1))
    assert(math.isclose(slope(0, 2, 5, -2), -0.8))
    