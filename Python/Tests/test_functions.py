import pytest
from Modules import functions

def test_maxi():
    assert functions.maxi(1,2,3) == 3
    assert functions.maxi(3,2,3) == 3
    assert functions.maxi(1.1,1.2,1.3) == 1.3
    assert functions.maxi('1','2','3') == 3
