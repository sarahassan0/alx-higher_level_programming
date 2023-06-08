#!/usr/bin/python3
from sys import argv
count = 0
for i in argv[1:]:
    count += int(i)
print(count)
