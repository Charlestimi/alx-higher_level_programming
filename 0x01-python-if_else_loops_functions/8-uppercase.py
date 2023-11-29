#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            c = ord(i) - 32
        else:
            c = ord(i)
        upper += chr(c)
    print(upper)

