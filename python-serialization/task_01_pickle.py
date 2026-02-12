#!/usr/bin/env python3
"""
task_01_pickle.py

Ce module montre comment sérialiser et désérialiser des objets personnalisés
en Python en utilisant le module pickle.
"""

import pickle  # Import du module pickle pour la sérialisation binaire

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except:
            return None
