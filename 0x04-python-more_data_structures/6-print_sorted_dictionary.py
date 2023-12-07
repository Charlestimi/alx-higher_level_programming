#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dictionary = sorted(a_dictionary.keys())
    for i in new_dictionary:
        print('{}: {}'.format(i, a_dictionary[i]))
