#!/usr/bin/python3
"""
Module that defines a class MyList that inherits from list.
Provides a method print_sorted() that prints the list sorted in ascending order.
"""


class MyList(list):
    """
    A subclass of the built-in list type.
    Adds a public instance method print_sorted() that prints
    the list elements sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order without modifying the original list.
        """
        print(sorted(self))
