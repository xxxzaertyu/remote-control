from flask import Flask, request
import os

app = Flask(__name__)


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


port = int(os.environ.get("PORT", 5000))

app.run(
    host="0.0.0.0",
    port=port
)