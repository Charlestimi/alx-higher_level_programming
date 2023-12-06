#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in matrix:
            for number in row:
                if number != len(row) - 1:
                    print()
                print("{:d}".format(row[number]), end=" ")
            print()
