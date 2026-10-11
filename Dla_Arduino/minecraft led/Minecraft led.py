import time
import json
import re
import serial
import os

logs = r"C:\Users\adamavenix\AppData\Roaming\.dawn\profiles\feather-default--1-21-4\.minecraft\logs\latest.log"
last_kill_time = None
arduino = serial.Serial("COM7",timeout=2,baudrate=9600)
arduino.reset_input_buffer()
arduino.reset_output_buffer()
color = 'white'
def load_config():
        with open("config.json", "r", encoding="utf-8") as fi:
            return json.load(fi)
f = open(logs, "r", encoding="utf-8", errors="ignore")
f.seek(0, os.SEEK_END)
templates =load_config()["wzorce_zabojstw"]
try:
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.01)
        if "[Sound engine/" in line:
            continue

        if any(re.search(template,line) for template in templates):
            time_now = time.time()
            if last_kill_time is None:
                time_of_kill = 999
            else:
                time_of_kill = time_now - last_kill_time

            if  time_of_kill > 30:
                color = "green"
                print("green")
            elif  time_of_kill > 20:
                color = "yellow"
                print("yellow")
            elif time_of_kill > 10: # jezeli minie 5s od ostatniego killa wyswietlaj normalnie
                color = "orange"
                print("orange")
            elif  time_of_kill < 10:
                # Kille byly szybko sprawdzamy czy przeczytal sie 2 razy ten sam gracz
                color = "red"
                print("red")
            print(time_of_kill)
            arduino.write(f"{color}\n".encode())
            last_kill_time = time_now

except KeyboardInterrupt:
    f.close()