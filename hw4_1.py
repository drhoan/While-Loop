# Please write a program which asks user to enter a integer number.
# The program should keep asking for numbers until the user types in zero.
# The program then stop asking and print "Finish"
# Hint: use while True: structure
# A sample output is below
"""
Enter an integer number: 2
Enter an integer number: 3
Enter an integer number: 0
Finish
"""

while True:
    a = int(input("Enter an integer number: "))
    if a == 0:
        break

print("Finish")