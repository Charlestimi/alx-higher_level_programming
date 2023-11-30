#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = len(sys.argv)
    add = 0
if count == 1:
    add = 0
else:
    for i in range(1, count):
        add += int(sys.argv[i])
print("{:d}".format(add))
