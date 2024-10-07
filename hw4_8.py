# Please write a program which keeps asking the user for a PIN code numbers until they type in the correct one, which is 4321.
# The program should then print out the number of times the user tried different codes.
# Sample output is shown below:
"""
PIN: 3245
Wrong
PIN: 1234
Wrong
PIN: 0000
Wrong
PIN: 4321
Correct! It took you 4 attempts
"""
# If the user gets it right on the first try, the program should print out something a bit different:
"""Correct! It only took you one single attempt!"""
PIN = 4321
count = 0
while True:
    a = int(input("PIN: "))
    count += 1
    if a == PIN:
        if count == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print("Correct! It took you", count, "attempts")
        break
    else:
        print("Wrong")