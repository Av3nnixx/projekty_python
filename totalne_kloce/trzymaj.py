import pyautogui
import keyboard

print("Program uruchomiony. Czekam na kliknięcie 'o'...")

keyboard.wait('o')

pyautogui.mouseDown()
print("Myszka została wciśnięta i trzyma!")