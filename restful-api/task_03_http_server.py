# task_03_http_server.py

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Un gestionnaire HTTP simple qui gère quelques endpoints."""

    def do_GET(self):
        """Gère les requêtes GET envoyées au serveur."""

        # Endpoint racine "/"
        if self.path == "/":
            self.send_response(200)  # Code HTTP 200 = OK
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            message = "Hello, this is a simple API!"
            self.wfile.write(message.encode("utf-8"))

        # Endpoint "/data"
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode("utf-8"))

        # Endpoint "/status"
        elif self.path == "/status":
            status = {"status": "OK"}
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(status).encode("utf-8"))

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

        # Si le chemin demandé n’est pas reconnu → 404
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            error_message = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_message).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """Démarre le serveur HTTP sur le port indiqué."""
    server_address = ("", port)  # "" = écoute sur toutes les interfaces réseau
    httpd = server_class(server_address, handler_class)
    print(f"✅ Server running on http://localhost:{port}")
    try:
        httpd.serve_forever()  # Boucle infinie : attend les requêtes
    except KeyboardInterrupt:
        print("\n🛑 Server stopped manually.")
    finally:
        httpd.server_close()


if __name__ == "__main__":
    run()
