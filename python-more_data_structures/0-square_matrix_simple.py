#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 0-square_matrix_simple
This module defines a function that computes the square value
of all integers of a matrix.
"""


def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.

    Args:
        matrix (list of lists): 2D array of integers.

    Returns:
        list of lists: A new matrix where each value is squared.
    """
    new_matrix = []
    for row in matrix:
        new_row = [x ** 2 for x in row]
        new_matrix.append(new_row)
    return new_matrix
