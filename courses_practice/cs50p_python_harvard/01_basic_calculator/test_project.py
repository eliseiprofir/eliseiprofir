import pytest
from project import add, sub, mul, div

def main():
    test_add()
    test_sub()
    test_mul()
    test_div()

def test_add():
    assert add(3, 2) == 5.0
    assert add(3, 0) == 3.0
    assert add('s', 1) == "ERROR: Not a valid number. Try again!"

def test_sub():
    assert sub(6, 3) == 3.0
    assert sub(50, 20) == 30.0
    assert add(2, 's') == "ERROR: Not a valid number. Try again!"

def test_mul():
    assert mul(5, 10) == 50.0
    assert mul(20, 2) == 40.0
    assert add('s', 1) == "ERROR: Not a valid number. Try again!"

def test_div():
    assert div(10, 5) == 2.0
    assert div(10, 0) == "You cannot divide by 0."
    assert add('s', 2) == "ERROR: Not a valid number. Try again!"

if __name__ == "__main__":
    main()