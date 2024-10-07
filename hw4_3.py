# Please write a program which asks the user for integer numbers.
# If the number is below zero, the program should print out the message "Invalid number".
# If the number is above zero, the program should print out the square root of the number using the Python sqrt function.
# In either case, the program should then keep asking for another number.
# If the user inputs the number zero, the program should stop asking for numbers and print "Exiting".
# Sample output is shown below:
"""
Please type in a number: 16
4.0
Please type in a number: 4
2.0
Please type in a number: -3
Invalid number
Please type in a number: 1
1.0
Please type in a number: 0
Exiting
"""

while True:
    num = int(input("Please type in a number: "))
    if num == 0:
        print("Exiting")
        break
    elif num < 0:
        print("Invalid number")
    else:
        print(num ** 0.5)