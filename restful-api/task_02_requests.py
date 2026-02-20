# task_02_requests.py

import requests
import csv
from typing import List, Dict

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts() -> None:
    """
    Récupère tous les posts depuis JSONPlaceholder et affiche le status code
    puis les titres de chaque post.
    """
    try:
        response = requests.get(BASE_URL, timeout=10)
    except requests.RequestException as e:
        print(f"Erreur de requête : {e}")
        return

    print(f"Status Code: {response.status_code}")

    if not response.ok:
        print(f"Requête échouée avec le code {response.status_code}")
        return

    try:
        posts = response.json()
    except ValueError:
        print("Réponse non JSON ou JSON mal formé.")
        return

    for post in posts:
        # sécuriser l'accès aux clefs en utilisant .get()
        title = post.get("title", "")
        print(title)


def fetch_and_save_posts() -> None:
    """
    Récupère tous les posts depuis JSONPlaceholder et les sauvegarde dans posts.csv
    avec les colonnes : id, title, body.
    """
    try:
        response = requests.get(BASE_URL, timeout=10)
    except requests.RequestException as e:
        print(f"Erreur de requête : {e}")
        return

    if not response.ok:
        print(f"Requête échouée avec le code {response.status_code}")
        return

    try:
        posts_raw = response.json()
    except ValueError:
        print("Réponse non JSON ou JSON mal formé.")
        return

    # Construire une liste de dictionnaires avec uniquement id, title et body
    posts: List[Dict[str, object]] = [
        {"id": post.get("id"), "title": post.get("title", ""), "body": post.get("body", "")}
        for post in posts_raw
    ]

    csv_filename = "posts.csv"
    try:
        with open(csv_filename, mode="w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts)
    except OSError as e:
        print(f"Erreur d'écriture du fichier {csv_filename} : {e}")
        return

    print(f"{len(posts)} posts sauvegardés dans {csv_filename}.")
