#!/usr/bin/python3
"""
Module that defines the BaseGeometry class.
Adds a method area() that raises an Exception.
"""


class BaseGeometry:
    """
    Base class for geometry-related operations.
    This version defines an area() method that must be implemented
    by subclasses.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        This method is meant to be overridden by subclasses.
        """
