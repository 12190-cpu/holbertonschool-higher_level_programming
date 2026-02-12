#!/usr/bin/python3
"""Module Student that defines a student with serialization and deserialization."""

class Student:
    """Class that defines a student with public attributes."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): First name of the student
            last_name (str): Last name of the student
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to include.
                                     If None, all attributes are included.

        Returns:
            dict: Dictionary containing selected attributes of the student.
        """
        student_dict = vars(self)  # vars(self) récupère tous les attributs publics
        if attrs is None:
            return student_dict
        else:
            # Filtrer uniquement les attributs présents dans attrs
            filtered_dict = {k: v for k, v in student_dict.items() if k in attrs}
            return filtered_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a dictionary.

        Args:
            json (dict): Dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)  # Définit dynamiquement les attributs
