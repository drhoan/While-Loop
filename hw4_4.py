# The below program should print out a countdown.
# Output should look like this
"""
Countdown!
5
4
3
2
1
Now!
"""
# However, the is a bug in the program and the output is not correct. Please fix it to get the above output.
number = 5
print("Countdown!")
while True:
    print(number)
    number = number - 1
    if number > 0:
        break
print("Now!")