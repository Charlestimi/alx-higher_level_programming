#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for idn in range(x):
        try:
            print(my_list[idn], end="")
            counter += 1
        except (Exception):
            break
    print()
    return counter
