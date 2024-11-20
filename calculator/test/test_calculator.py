import pytest

import sys
import os

# Add the `calculator/src` directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from calculator import add, subtract, multiply, divide, power



def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 3) == -3

def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(0, 1) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 1) == 5
    with pytest.raises(ValueError):
        divide(5, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
