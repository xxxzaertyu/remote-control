import mss
from PIL import Image
import time
import requests

SERVER_URL = "http://127.0.0.1:5000/upload"

with mss.mss() as sct:
    monitor = sct.monitors[1]

    while True:
        screenshot = sct.grab(monitor)

        image = Image.frombytes(
            "RGB",
            screenshot.size,
            screenshot.rgb
        )

        image.save("screen.png")

        with open("screen.png", "rb") as file:
            response = requests.post(
                SERVER_URL,
                files={"screen": file}
            )

        print("Capture envoyée !")

        time.sleep(5)