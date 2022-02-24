import pytest


  # that this is where the data is coming from
@pytest.fixture
def data():
    
    data = [1,2,3]
    
    return data


def test_case_1(data):
    assert data[2]==3
    
def test_case_2(data):
    assert data[0] ==2
    
 

