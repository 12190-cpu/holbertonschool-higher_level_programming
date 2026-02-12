#!/usr/bin/python3
"""Module that generates Pascal's triangle."""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.

    Args:
        n (int): The number of rows of Pascal's triangle.

    Returns:
        list of lists of integers: Pascal's triangle with n rows.
        Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []  # Liste qui contiendra toutes les lignes du triangle

    for row_num in range(n):
        # Chaque ligne commence par des 1
        row = [1] * (row_num + 1)

        # Calcul des valeurs internes de la ligne
        for j in range(1, row_num):
            # Chaque élément est la somme des deux éléments juste au-dessus
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

        # Ajout de la ligne complète au triangle
        triangle.append(row)

    return triangle
