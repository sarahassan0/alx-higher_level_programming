#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv
    count = 0
    for i in argv[1:]:
        count += int(i)
    print("{:d}".format(count))
