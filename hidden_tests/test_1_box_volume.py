from q1_box_volume import box_volume 

def test_box_volume():
    
    # Visible test    
    assert(box_volume(3, 4, 2) == 24)
    assert(box_volume(2, 2, 2) == 8)
    assert(box_volume(5, 2, 0) == 0)
    

