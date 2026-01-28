#!/usr/bin/python3
"""
This module defines a Square class with a validated private size attribute
and a public method to compute the area of the square.
"""


class Square:
    """
    This class defines a square.

    The size attribute is private and validated to ensure it is a
    non-negative integer. The class also provides a public method
    to calculate the area of the square.
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

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The current area of the square.
        """
        return self.__size * self.__size
