#!/usr/bin/python3
"""
This module defines a Rectangle class with private width and height,
methods to compute area, perimeter, print the rectangle using '#',
a class attribute number_of_instances, and a message when deleted.
"""


class Rectangle:
    """Represents a rectangle with width and height."""

    # Public class attribute to track number of Rectangle instances
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle with optional width and height."""
        self.width = width
        self.height = height
        # Increment the class attribute when a new instance is created
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle. If width or height is 0, perimeter is 0."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the rectangle as a string of '#' characters.

        If width or height is 0, return an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for _ in range(self.height))

    def __repr__(self):
        """Return a string representation that can recreate a new instance using eval()."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when a Rectangle instance is deleted and decrement number_of_instances."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
