#!/usr/bin/python3
"""
Retourne la liste des attributs et méthodes disponibles pour un objet.
Ce module fournit la fonction lookup(obj) qui renvoie une liste.
"""


def lookup(obj):
    """
    Retourne la liste des attributs et méthodes (noms) de l'objet fourni.

    Args:
        obj: Tout objet Python (classe, instance, type builtin, ...)

    Returns:
        list: Liste triée des noms des attributs et méthodes disponibles.
    """
    return dir(obj)
