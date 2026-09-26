import websocket

SERVER_URL = "wss://remote-control-rpec.onrender.com/ws"

print("Connexion au serveur...")

try:
    ws = websocket.create_connection(
        SERVER_URL,
        timeout=10
    )

    print("Connecté à Render !")

    ws.send("PC2_CONNECTED")

    while True:
        message = ws.recv()

        if message is None:
            break

        print("Message reçu :", message)

except Exception as e:
    print("Connexion impossible :", e)

finally:
    try:
        ws.close()
    except:
        pass