import pyautogui
import time

print("Contrôle de test dans 3 secondes...")
time.sleep(3)

x, y = pyautogui.position()

print(f"Position actuelle : {x}, {y}")

pyautogui.moveTo(x + 200, y, duration=1)

print("Souris déplacée !")