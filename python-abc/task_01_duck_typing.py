#!/usr/bin/env python3
"""
task_01_duck_typing.py

Définit une classe abstraite Shape (avec area et perimeter),
deux implémentations concrètes Circle et Rectangle, et la
fonction shape_info qui affiche l'aire et le périmètre
en s'appuyant sur le duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Classe abstraite représentant une forme géométrique.

    Les sous-classes doivent implémenter les méthodes `area`
    et `perimeter`.
    """

    @abstractmethod
    def area(self):
        """Retourne l'aire de la forme (doit être implémenté)."""
        pass

    @abstractmethod
    def perimeter(self):
        """Retourne le périmètre de la forme (doit être implémenté)."""
        pass


class Circle(Shape):
    """Cercle défini par un rayon."""

    def __init__(self, radius):
        """Initialise le cercle avec un rayon (float ou int)."""
        self.radius = radius

    def area(self):
        """Retourne l'aire du cercle : π * r^2."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Retourne la circonférence (périmètre) : 2 * π * r."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle défini par une largeur et une hauteur."""

    def __init__(self, width, height):
        """Initialise le rectangle avec width et height (float ou int)."""
        self.width = width
        self.height = height

    def area(self):
        """Retourne l'aire du rectangle : width * height."""
        return self.width * self.height

    def perimeter(self):
        """Retourne le périmètre : 2 * (width + height)."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Affiche l'aire et le périmètre de l'objet passé.

    Ne vérifie pas explicitement le type ; s'appuie sur duck typing :
    l'objet doit juste fournir les méthodes `area()` et `perimeter()`.
    """

