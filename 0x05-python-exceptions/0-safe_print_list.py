#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for idn in range(0, x):
        try:
            print(my_list[idn], end="")
            count += 1
        except(Exception):
            pass
        print()
        return counter
