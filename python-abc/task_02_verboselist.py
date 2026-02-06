#!/usr/bin/env python3
"""
task_02_verboselist.py

Définit une classe VerboseList qui hérite de la classe list
et affiche des messages à chaque modification (ajout/suppression).
"""


class VerboseList(list):
    """Une liste étendue qui affiche des notifications
    lorsque des éléments sont ajoutés ou retirés.
    """

    def append(self, item):
        """Ajoute un élément et affiche un message."""
        super().append(item)  # Appel de la méthode append originale
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Étend la liste avec plusieurs éléments et affiche un message."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Supprime un élément et affiche un message."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)  # Appel de la méthode remove originale

    def pop(self, index=-1):
        """Supprime et renvoie un élément, en affichant un message."""
        item = self[index]  # On récupère la valeur avant suppression
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
