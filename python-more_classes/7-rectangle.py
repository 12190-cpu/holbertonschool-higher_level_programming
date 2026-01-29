#!/usr/bin/python3
"""
This module defines a Rectangle class with private width and height,
tracks the number of instances, supports a printable symbol for
string representation, and prints a message when an instance is deleted.
"""


class Rectangle:
    """Represents a rectangle with width and height."""

    # public class attribute: counts instances
    number_of_instances = 0
    # public class attribute: symbol used for string representation
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is negative.
        """
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
        """Set the height of the rectangle with validation.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle.

        If width or height is 0, perimeter is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the rectangle as a string using the print_symbol.

        If width or height is 0, return an empty string.
        The symbol used is the value of self.print_symbol (instance override
        if present) converted to str() and repeated width times per line.
        """
        if self.width == 0 or self.height == 0:
            return ""
        line = str(self.print_symbol) * self.width
        return "\n".join(line for _ in range(self.height))

    def __repr__(self):
        """Return a string representation able to recreate a new instance."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Called when an instance is about to be destroyed.

        Prints a goodbye message and decrements the instance counter.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
