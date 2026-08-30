from q5_compute_total import compute_total 


def test_compute_total():
    import math # we use math.isclose to compare floats
    assert(math.isclose(compute_total(12, 0.05), 12.6))
    assert(math.isclose(compute_total(15, 0.07), 16.05))
    assert(math.isclose(compute_total(5.75, 0), 5.75))

