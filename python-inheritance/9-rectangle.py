#!/usr/bin/python3
"""
Module that defines the Rectangle class,
which inherits from BaseGeometry.
Implements area() and __str__ methods.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    Validates width and height, implements area() and string representation.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with validated width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns:
            int: The area (width * height)
        """
        return self.__width * self.__height
