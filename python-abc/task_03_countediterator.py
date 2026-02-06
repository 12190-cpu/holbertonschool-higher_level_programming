#!/usr/bin/env python3
"""
task_03_countediterator.py

Définit la classe CountedIterator, une extension du comportement
d'un itérateur Python classique, qui garde la trace du nombre
d'éléments déjà itérés.
"""


class CountedIterator:
    """Itérateur qui garde le compte des éléments parcourus."""

    def __init__(self, iterable):
        """Initialise l'itérateur à partir d'un itérable et un compteur."""
        self.iterator = iter(iterable)  # Crée un itérateur standard sur l’objet
        self.count = 0  # Initialise le compteur à zéro

    def __next__(self):
        """Renvoie le prochain élément et incrémente le compteur."""
        # On essaie de récupérer l’élément suivant dans l’itérateur interne
        try:
            item = next(self.iterator)
            self.count += 1  # Incrémente le compteur à chaque appel
            return item
        except StopIteration:
            # Si l’itérateur interne est épuisé, on relance l’exception
            raise StopIteration

    def get_count(self):
        """Retourne le nombre d’éléments déjà itérés."""
        return self.count

