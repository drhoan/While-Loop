# One way of computing square roots is Newton’s method.
# Suppose that you want to know the square root of n.
# If you start with almost any approximation, e.g. approx = 1/2*n,
# you can compute a better approximation with the following formula:
# better_approx =  1/2 * (approx + n/approx)
# using this better_approx, you can compute an even better_approx and so on.
# Write function newtonSqrt to calculate square root of a number n using the above method.
# Loop until the difference between approx and better_approx is less than 0.0001.
# Then return the result
# Call your function with n = 9 or 25 or 100, etc. and print the result.
# Hint: you may want to print out your approximate after each iteration to "debug" your program.

def newtonSqrt(n):
    # TO DO: type your docstring here
    
    # TO DO: type your code here


if __name__ == "__main__":
    print(newtonSqrt(9))  # should print 3.0000000000393214 or similar
    print(newtonSqrt(25))  # should print 5.000000000016778 or similar
    print(newtonSqrt(100))  # should print 10.000000000107445 or similar