from q7_nth_fibnonacci_number import nth_fibonacci_number 


""" Test 7 """
def test_nth_fibonacci_number():
    print("Testing nth_fibonacci_number...", end="")
    assert(nth_fibonacci_number(1) == 1)
    assert(nth_fibonacci_number(3) == 2)
    assert(nth_fibonacci_number(7) == 13)
    assert(nth_fibonacci_number(10) == 55)
    print("... done!")
