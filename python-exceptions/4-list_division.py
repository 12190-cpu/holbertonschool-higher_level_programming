#!/usr/bin/python3
"""
4-list_division.py
Divides element by element two lists safely using try/except/finally.
"""


def list_division(my_list_1, my_list_2, list_length):
    """
    Divides elements of my_list_1 by elements of my_list_2 element-wise.

    Args:
        my_list_1 (list): First list of numbers (any type)
        my_list_2 (list): Second list of numbers (any type)
        list_length (int): Number of elements to process

    Returns:
        list: A new list of divisions, 0 if error occurs
    """
    result = []

    for i in range(list_length):
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except TypeError:
            print("wrong type")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            result.append(div)

    return result
