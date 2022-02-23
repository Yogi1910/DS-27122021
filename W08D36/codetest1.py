import pytest

@pytest.fixture
def pre_data():
    data = {'scooty':2,'rickshaw':3,'car':4}
    return data

def test_case_1(pre_data):
    assert pre_data['scooty'] == 2


def test_case_2(pre_data):
    assert pre_data['car']==4

    
    
