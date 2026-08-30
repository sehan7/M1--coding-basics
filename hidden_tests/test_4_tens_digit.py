from q4_tens_digit import tens_digit 


def test_tens_digit():
    assert(tens_digit(1234) == 3)
    assert(tens_digit(42) == 4)
    assert(tens_digit(9) == 0)

