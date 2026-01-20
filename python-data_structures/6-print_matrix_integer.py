#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 6-print_matrix_integer
This module defines a function that prints a matrix of integers.
"""

def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.

    Args:
        matrix (list of lists): A 2D list (matrix) of integers.
    """
    for row in matrix:
        for i in range(len(row)):
            if i < len(row) - 1:
                print("{:d}".format(row[i]), end=" ")
            else:
                print("{:d}".format(row[i]), end="")
        print()
