# Prime number is a number that is greater than 1 and has no divisors other than 1 and itself.
# Write a program that checks if the number is a prime number.
# If the number is a prime number, the program should return True.
# If the number is not a prime number, the program should return False.
# Hint: you can use for loop and modulus operator.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print(is_prime(0))  # should print False
    print(is_prime(1))  # should print False
    print(is_prime(2))  # should print True
    print(is_prime(3))  # should print True
    print(is_prime(4))  # should print False