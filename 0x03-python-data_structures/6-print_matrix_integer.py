#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in matrix:
            for number in row:
                if number != row:
                    endspace = " "
                print("{:d}".format(number), end=endspace)
            print()
