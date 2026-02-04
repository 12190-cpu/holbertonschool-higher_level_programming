#!/usr/bin/python3
"""
Module that defines the BaseGeometry class.
This class provides a base for geometric operations and validations.
"""


class BaseGeometry:
    """
    Base class for geometry-related operations.
    Contains a placeholder area() method and an integer validator.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        This method is intended to be overridden by subclasses.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the parameter (always a string).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
