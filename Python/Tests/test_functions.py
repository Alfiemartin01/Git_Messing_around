from Modules.functions_ import maxi 

def test_maxi():
    assert maxi(1,2,3) == 3
    assert maxi(3,2,3) == 3
    assert maxi(1.1,1.2,1.3) == 1.3
    assert maxi('1','2','3') == 3

