#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_d = number % 10
if last_d > 5:
    print(f"last digit of {number:d} is {last_d} and is greater than 5")
elif last_digit == 0:
    print(f"last digit of {number:d} is {last_d} and is 0")
else:
    print(f"last digit of {number:d} is {last_d} and is less than 6 and not 0")