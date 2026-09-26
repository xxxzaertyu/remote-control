from flask import Flask, request
from flask_sock import Sock
import os

app = Flask(__name__)
sock = Sock(app)


@app.route("/")
def home():
    return "Serveur remote-control actif !"


@app.route("/upload", methods=["POST"])
def upload():
    if "screen" not in request.files:
        return "Aucune capture reçue", 400

    file = request.files["screen"]
    file.save("received_screen.png")

    print("Capture reçue !")

    return "OK"


@sock.route("/ws")
def websocket(ws):
    print("Connexion WebSocket établie !")

    while True:
        message = ws.receive()

        if message is None:
            print("Connexion fermée.")
            break

        print("Message reçu :", message)


port = int(os.environ.get("PORT", 5000))

app.run(
    host="0.0.0.0",
    port=port
)