import pytest
from hw4_7 import is_prime

def test_is_prime_prime_number():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True

def test_is_prime_non_prime_number():
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False

def test_is_prime_large_prime_number():
    assert is_prime(7919) == True

def test_is_prime_large_non_prime_number():
    assert is_prime(8000) == False

def test_is_prime_negative_number():
    assert is_prime(-1) == False
    assert is_prime(-10) == False

def test_is_prime_zero():
    assert is_prime(0) == False

# Add more test cases as needed
if __name__ == "__main__":
    test_is_prime_prime_number()
    test_is_prime_non_prime_number()
    test_is_prime_large_prime_number()
    test_is_prime_large_non_prime_number()
    test_is_prime_negative_number()
    test_is_prime_zero()
    print("All tests passed")