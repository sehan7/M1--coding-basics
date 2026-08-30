from q8_number_bills_needed import number_bills_needed 

def test_number_bills_needed():
    assert(number_bills_needed(42) == 2 + 0 + 2)
    assert(number_bills_needed(17) == 0 + 3 + 2)
    assert(number_bills_needed(79) == 3 + 3 + 4)
    assert(number_bills_needed(4) == 0 + 0 + 4)
    assert(number_bills_needed(5) == 0 + 1 + 0)
