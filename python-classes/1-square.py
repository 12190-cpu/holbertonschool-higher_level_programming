#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.

The Square class represents a square shape and stores its size as a
private instance attribute to ensure controlled access and modification.
"""


class Square:
    """
    This class defines a square.

    The size of the square is stored as a private attribute to prevent
    direct access from outside the class. This allows validation and
    control in future implementations.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size: The size of the square (no type or value verification
            is done at this stage).
        """
        self.__size = size
