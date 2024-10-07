# Write a program that print out the message "hi" and then ask "Shall we continue?".
# If user input is different from "no", the program will repeat the question until the user inputs "no".
# Then the program should print out "okay then" and finish. Please have a look at the example below.
"""
hi
Shall we continue? yes
hi
Shall we continue? oui
hi
Shall we continue? jawohl
hi
Shall we continue? no
okay then
"""

while True:
    print("hi")
    a = input("Shall we continue? ")
    if a == "no":
        break
print("okay then")