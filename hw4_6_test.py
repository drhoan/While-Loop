import pytest
from hw4_6 import newtonSqrt

def test_newtonSqrt_positive():
    result = newtonSqrt(25)
    assert result == pytest.approx(5, rel=1e-3)

def test_newtonSqrt_zero():
    result = newtonSqrt(0)
    assert result == pytest.approx(0, rel=1e-4)

def test_newtonSqrt_small_number():
    result = newtonSqrt(0.0001)
    assert result == pytest.approx(0.01, rel=1e-4)

def test_newtonSqrt_large_number():
    result = newtonSqrt(1e10)
    assert result == pytest.approx(1e5, rel=1e-4)

def test_newtonSqrt_non_perfect_square():
    result = newtonSqrt(2)
    assert result == pytest.approx(1.414213562, rel=1e-4)

if __name__ == "__main__":
    test_newtonSqrt_positive()
    # test_newtonSqrt_zero()
    test_newtonSqrt_small_number()
    test_newtonSqrt_large_number()
    test_newtonSqrt_non_perfect_square()
    print("All tests passed")