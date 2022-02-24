def fun(x):
    if x%2==0:
        return x+5

    else:
        return x-5


import pytest
        
def test_method():
    assert fun(3)==8


def test_method_2():
    assert fun(2) ==7

def test_case():
    assert fun(4)==9

@pytest.mark.kalpesh
def test_case_2():
    assert fun(5)==0
    
