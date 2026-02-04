#!/usr/bin/python3
"""
Module that defines the Square class,
which inherits from Rectangle.
Implements size validation, area calculation,
and custom string representation.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    Validates size, implements area(), and custom __str__().
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

    def __str__(self):
        """
        Returns a string representation of the Square
        in the format: [Square] <width>/<height>
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
