import webbrowser
import time
import pygame
import threading
def muzyka():
    timer1 = 0
    while timer1 < 3:
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", )
        time.sleep(0.5)
        timer1 += 1

def bros_open():
    while True:
        pygame.mixer.music.load("RickRoll.MP3")
        pygame.mixer.music.play()
        time.sleep(208)
pygame.mixer.init()
muz = threading.Thread(target = muzyka)
muz.start()
bro = threading.Thread(target= bros_open())
bro.start()