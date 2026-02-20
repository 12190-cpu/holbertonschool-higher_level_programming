#!/usr/bin/env python3
"""
task_03_http_server.py
Créer une API simple avec http.server
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Un gestionnaire HTTP qui gère différents endpoints."""

    def do_GET(self):
        """Gère les requêtes GET et répond selon le chemin demandé."""

        # Endpoint racine "/"
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # Endpoint "/data" -> retourne un JSON
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))

        # Endpoint "/status"
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"OK")

        # Endpoint "/info"
        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode("utf-8"))

        # Autres endpoints non définis
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            error_msg = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_msg).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """Démarre le serveur HTTP sur le port 8000"""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"✅ Server running on http://localhost:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped manually.")
    finally:
        httpd.server_close()


if __name__ == "__main__":
    run()
