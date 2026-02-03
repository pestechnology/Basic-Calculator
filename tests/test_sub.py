import pytest
from calculator.sub import subtract

def test_subtract_two():
    assert subtract(10, 5) == 5

def test_subtract_multiple():
    assert subtract(20, 5, 3, 2) == 10

def test_subtract_one_input_error():
    with pytest.raises(ValueError):
        subtract(10)
