from q2_make_introduction import make_introduction 

""" Test 2 """
def test_make_introduction():
    
    assert(make_introduction("Nnenna", "swimming") == "My name is Nnenna and I like swimming")
    assert(make_introduction("Sigurd", "cooking") == "My name is Sigurd and I like cooking")
    assert(make_introduction("Rei", "reading") == "My name is Rei and I like reading")
    assert(make_introduction("Govind", "dancing") == "My name is Govind and I like dancing")
    