#!/usr/bin/python3
"""Module Student that defines a student with optional JSON filtering."""


class Student:
    """Class that defines a student with first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): Student's first name
            last_name (str): Student's last name
            age (int): Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to include.
                                     If None, include all attributes.

        Returns:
            dict: Dictionary containing selected attributes of the student.
        """
        student_dict = vars(self)  # Récupère tous les attributs de l'instance
        if attrs is None:
            return student_dict  # Si pas de filtre, retourne tout
        else:
            # Retourne uniquement les attributs existants dans la liste attrs
            filtered_dict = {k: v for k, v in student_dict.items() if k in attrs}
            return filtered_dict
