#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
print("Last digit of {} ".format(number), end="")
last_digit = abs(number) % 10
if number < 0:
    last_digit = last_digit * -1

if last_digit > 5:
    print("is {} and is greater than 5".format(last_digit))
elif last_digit == 0:
    print("is {} and is 0".format(last_digit))
else:
    print("is {} and is less than 6 and not 0".format(last_digit))
