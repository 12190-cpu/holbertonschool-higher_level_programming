#!/usr/bin/env python3
"""
task_05_dragon.py

Démonstration de l'utilisation des Mixins en Python.
On crée deux mixins (SwimMixin et FlyMixin) et une classe Dragon
qui hérite de ces deux mixins pour combiner leurs comportements.
"""


class SwimMixin:
    """Mixin fournissant la capacité de nager."""

    def swim(self):
        """Affiche un message indiquant que la créature nage."""
        print("The creature swims!")


class FlyMixin:
    """Mixin fournissant la capacité de voler."""

    def fly(self):
        """Affiche un message indiquant que la créature vole."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Classe représentant un dragon capable de nager et de voler."""

    def roar(self):
        """Affiche un message indiquant que le dragon rugit."""
        print("The dragon roars!")
