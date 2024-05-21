import pytest
from solution import ParkingSystem


@pytest.mark.parametrize("test_input, expected", [
])
def test_solution(test_input, expected):
    pass

def test_custom():
    s = ParkingSystem(1, 1, 0)
    assert s.addCar(1) == True
    assert s.addCar(2) == True
    assert s.addCar(3) == False
    assert s.addCar(1) == False
    assert s.addCar(2) == False
    assert s.addCar(3) == False
