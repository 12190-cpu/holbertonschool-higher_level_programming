#!/usr/bin/env python3
"""
task_04_flyingfish.py

Montre un exemple d'héritage multiple en Python
à travers les classes Fish, Bird et FlyingFish.
"""


class Fish:
    """Classe représentant un poisson."""

    def swim(self):
        """Affiche un message indiquant que le poisson nage."""
        print("The fish is swimming")

    def habitat(self):
        """Affiche l'habitat naturel du poisson."""
        print("The fish lives in water")


class Bird:
    """Classe représentant un oiseau."""

    def fly(self):
        """Affiche un message indiquant que l'oiseau vole."""
        print("The bird is flying")

    def habitat(self):
        """Affiche l'habitat naturel de l'oiseau."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Classe représentant un poisson volant, héritant de Fish et Bird."""

    def swim(self):
        """Redéfinit la méthode swim pour le poisson volant."""
        print("The flying fish is swimming!")

    def fly(self):
        """Redéfinit la méthode fly pour le poisson volant."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Redéfinit la méthode habitat pour le poisson volant."""
        print("The flying fish lives both in water and the sky!")
