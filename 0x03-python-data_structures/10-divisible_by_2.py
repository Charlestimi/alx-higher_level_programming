#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_lists = my_list
    if not my_list:
        return None
    for num in range(len(my_lists)):
        if my_lists[num] % 2 == 0:
            return my_lists, True
        else:
            return my_lists, False
