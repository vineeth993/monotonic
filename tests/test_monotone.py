from monotone import monotone
import pytest

def test1_monotone_min():
    list = [0, -1, -1, -3, 1, 1.3, 2.3, 3]
    assert monotone.monotone_min(list) == -3

def test2_montone_min_first():
    list = [1, 2, 3, 0, -1, -2]
    
    with pytest.raises(ValueError) as info:
        monotone.monotone_min(list)
    assert "Fist Half" in str(info.value)

def test3_montone_min_second():
    list = [0, -1, -2, 1, 3, 4, 2]
    
    with pytest.raises(ValueError) as info:
        monotone.monotone_min(list)
    assert "Second Half" in str(info.value)