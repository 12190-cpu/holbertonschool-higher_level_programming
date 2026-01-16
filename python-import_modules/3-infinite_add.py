#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # ignore argv[0] qui est le nom du script
    total = 0
    for num in argv:
        total += int(num)  # convertir chaque argument en entier et l’ajouter à total
    print(total)
