#!/usr/bin/python3
"""
Module that defines the Square class,
which inherits from Rectangle.
Implements size validation and area calculation.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    Validates size and implements area().
    """

    def __init__(self, size):
        """
        Initializes a Square instance with validated size.

        Args:
            size (int): The size of the square sides.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
