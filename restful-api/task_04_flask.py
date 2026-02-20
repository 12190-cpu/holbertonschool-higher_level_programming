# task_04_flask.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionnaire en mémoire pour stocker les utilisateurs
# ⚠️ Ne pas inclure de données initiales dans ton push vers le repo
users = {}


@app.route("/")
def home():
    """Route racine : affiche un message de bienvenue"""
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """Vérifie le statut de l'API"""
    return "OK"


@app.route("/data")
def get_usernames():
    """Retourne la liste de tous les usernames enregistrés"""
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/users/<username>")
def get_user(username):
    """Retourne les informations complètes d’un utilisateur spécifique"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Ajoute un nouvel utilisateur via une requête POST"""
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    # Si aucun corps JSON n’est fourni
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    # Validation des champs
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Création d’un nouvel utilisateur
    new_user = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", None),
        "city": data.get("city", "")
    }

    # Sauvegarde dans le dictionnaire
    users[username] = new_user

    # Réponse de succès
    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201


if __name__ == "__main__":
    # Démarrage du serveur Flask
    app.run(host="0.0.0.0", port=5000)
