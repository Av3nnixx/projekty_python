import time
import pyautogui
from pathlib import Path
from PIL import Image

folder = Path(__file__).parent

hotbar = {1: "sword",
          2: "pearls",
          3: "cobweb",
          4: "water",
          "R": "axe",
          "T": "wood",
          "G": "shield",
          "CapsLock": "pickaxe",
          "5": "gold_apple",
          "F": "totem"}

images = {}
results = []
time.sleep(2)
for k, v in hotbar.items():
    images[k] = Image.open(folder / f"{v}.png")
    res = pyautogui.locateOnScreen(images[k],confidence=0.8)
    results.append(res)
    if res is not None:
        center = pyautogui.center(res)
        pyautogui.moveTo(center)
        time.sleep(0.01)
        pyautogui.press(str(k))
    else:
        print("nie znaleziono")
    pyautogui.moveTo(938,426)
    time.sleep(0.01)

print(hotbar)   # nazwy plików bez zmian
print(results)   # wczytane obrazy