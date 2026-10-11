import pyautogui
import keyboard
import time
x = True
def spam(message,quantity):
    jump = 0
    for i in range(quantity):
        pyautogui.click(button="Left",x=227 ,y=348 + jump)
        pyautogui.write(message)
        pyautogui.press("enter")
        jump += 55
        time.sleep(0.2)
while True:
    ip = input("Wpisz co napisac: ")
    ilosc = int(input("DO ilu osob wyslac"))
    keyboard.wait("space")
    spam(ip, ilosc)

