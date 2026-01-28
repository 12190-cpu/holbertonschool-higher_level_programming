#!/usr/bin/python3
"""
This module defines a Square class with a validated private size attribute.

The Square class represents a square and ensures that its size is always
a non-negative integer by validating the input during instantiation.
"""


class Square:
    """
    This class defines a square.

    The size attribute is private and validated to ensure it is an
    integer greater than or equal to zero.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
