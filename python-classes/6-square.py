#!/usr/bin/python3
"""
This module defines a Square class with private size and position attributes,
including validation through property getters and setters. The class can
compute its area and print itself using the '#' character with a positional
offset.
"""


class Square:
    """
    This class defines a square.

    The square is defined by its size and its position (horizontal and vertical
    offset when printed). Both attributes are private and validated using
    property setters.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): A tuple of two positive integers
                representing the horizontal and vertical offset.

        Raises:
            TypeError: If size is not an integer or if position is invalid.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position
