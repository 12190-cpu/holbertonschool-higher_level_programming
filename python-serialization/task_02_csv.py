#!/usr/bin/env python3
"""
task_02_csv.py

Ce module permet de lire un fichier CSV et de le convertir en JSON
en utilisant les techniques de sérialisation de Python.
"""

import csv   # Module pour lire les fichiers CSV
import json  # Module pour sérialiser les objets Python en JSON

def convert_csv_to_json(csv_filename):
    try:
        data_list = []
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(row)

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4, ensure_ascii=False)

        return True
    except:
        return False