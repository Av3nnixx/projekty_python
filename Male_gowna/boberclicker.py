import ctypes
import pyautogui
import time
import threading
import keyboard
ctypes.windll.user32.SetProcessDPIAware()
stop = "running"
run = "stopping"
def close():
    global stop
    stop = "running"
    while not keyboard.is_pressed("["):
        time.sleep(0.01)
    print("zakonczono")
    stop = "stop"

def start():
    global run
    run = "stopping"
    while not keyboard.is_pressed("]"):
        time.sleep(0.01)
    run = "run"

def clicking(predkosci,ilosc_powtorzen):
    while run == "stopping":
        time.sleep(0.01)
    print("zaczeto")
    if predkosci == 0 or ilosc_powtorzen == 0:
        raise ValueError("nie dawaj tu 0 zjebie")
    czas = predkosci * ilosc_powtorzen
    czas = czas/60
    czas = round(czas,1)
    print(f"{czas}min")

    for i in range(ilosc_powtorzen):
        if stop == "stop":
            print("koniec")
            break
        pyautogui.click(button="left")
        time.sleep(predkosci)

def bober_click(predkosc,ilosc_powtorzen):
    chore3 = threading.Thread(target=start)
    chore3.start()
    chore1 = threading.Thread(target=close)
    chore1.start()
    chore2 = threading.Thread(
        target=clicking,
        args=(predkosc, ilosc_powtorzen)
    )
    chore2.start()
try:
    speed = float(input("Wprowadz speed: "))
    worktime = int(input("Wprowadz repeat quantity: "))
    print("Kliknij ] zeby zaczac")
except ValueError:
    print("Wpisalales zle dane")
    exit()
bober_click(speed,worktime)