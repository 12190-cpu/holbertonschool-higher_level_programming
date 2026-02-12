#!/usr/bin/env python3
"""
task_03_xml.py

Ce module montre comment sérialiser et désérialiser des dictionnaires Python
en utilisant le format XML avec le module xml.etree.ElementTree.
"""

import xml.etree.ElementTree as ET  # Module standard pour travailler avec XML

def serialize_to_xml(dictionary, filename):
    try:
        root = ET.Element("data")
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True
    except:
        return False

def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}
        for child in root:
            result[child.tag] = child.text
        return result
    except:
        return None
