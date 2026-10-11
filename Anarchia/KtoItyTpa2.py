# ===================== IMPORTY =====================
import keyboard,pyautogui,random,time,threading,os,atexit,datetime,json,sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame
from prettytable import PrettyTable
from pygame.mixer import Sound

# ===================== USTAWIENIA =====================
user_name = os.getlogin() # uzytkownik w dokumentach - windows
#ctypes.windll.user32.SetProcessDPIAware() # ustawienie skali ekranu

logs_Path = f"C:/Users/{user_name}/AppData/Roaming/.minecraft/logs/latest.log"
txt_path = "anarchiaDane.txt"
lunchers = {
    "feather"  :  f"C:/Users/{user_name}/AppData/Roaming/.minecraft/feather/logs/latest.log",
    "vanilla"  :  f"C:/Users/{user_name}/AppData/Roaming/logs/latest.log",

}
table = PrettyTable(["Data","Dzień","Godzina startu","Godzina końca","Czas pisania","Procent","Liczba napisań","Liczba próśb"])
start = False
writes_quantity = 0
pygame.mixer.init() #odpalenie dzwiekow

# ===================== FUNKCJE POMOCNICZE =====================
def get_base_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.abspath("")
def load_json():
    path = os.path.join(get_base_path(), "config.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def week_day():
    # zamienia index na dzien tygodnia
    dni = {
        0: "poniedziałek",
        1: "wtorek",
        2: "środa",
        3: "czwartek",
        4: "piątek",
        5: "sobota",
        6: "niedziela"
    }
    day = dni[datetime.datetime.now().weekday()]
    return day

def current_date(fulldate):
    #zwraca dane dnia np 1.03.2024 lub godzine  z minutami
    mo = datetime.datetime.now().month
    if mo < 10:
        mo = f"0{mo}"
    d = datetime.datetime.now().day
    h = datetime.datetime.now().hour
    mi = datetime.datetime.now().minute

    if mi < 10:
        mi = "0" + str(mi)

    if fulldate:
        return "{day}.{month}".format(day=d, month=mo)
    else:
        return "{hour}:{min}".format(hour=h, min=mi)


def wait():
    #czeka nieregularną ilość czasu
    x = random.randint(6, 7)
    y = random.randint(1, 10) / 10
    z = random.randint(1, 10) / 100
    sleep_time = x + y + z
    time.sleep(sleep_time)


# ===================== DŹWIĘKI / STEROWANIE =====================
def get_random_sound(folder, volume_value):
    base = get_base_path()
    folder_path = os.path.join(base, folder)

    if not os.path.exists(folder_path):
        print(f"Brak folderu: {folder_path}")
        return

    files = os.listdir(folder_path)
    if not files:
        print(f"Brak plików w: {folder_path}")
        return

    file_path = os.path.join(folder_path, files[0])
    sound = Sound(file_path)
    sound.set_volume(volume_value)
    sound.play()

def program_start():
    #gra dzwiek na start programu
    get_random_sound("start_sound", load_json()["start_volume"])
    #program znowu dziala
    global start
    start = True


def program_stop():
    #gra dzwiek na stop programu
    get_random_sound("stop_sound", load_json()["stop_volume"])
    #zatrzymuje program
    global start
    start = False
    print("zatrzymano")


def write_to_chat(button, text):
    pyautogui.press(button)
    keyboard.write(text)
    pyautogui.press("enter")


# ===================== LOGI / STATYSTYKI =====================
def tpaccepts(text):
    wish = "wysłał prośbe o teleportacje!"
    wishs_value = 0

    with open(text, "r", encoding="utf-8") as f:
        for line in f:
            if any(word in line for word in load_json()["friends_nicknames"]):
                #jezeli nickname kolegi to nie dodawaj 1
                continue
            if wish in line:
                #jezeli prosba w linijce dodaje 1
                wishs_value += 1
    # do testowania
    if wishs_value == 0:
        wishs_value += 1

    return wishs_value

#zwraca procenty skutecznosci pisania
def percentages(ac_tp,nickname):
    percentage = ac_tp / nickname * 100
    return f"{percentage:.2f}%"

#wydaje dzwiek gdy otrzymasz prosbe teleportacji

def got_request():
    last_request = []
    busy = False

    def check_requests():
        nonlocal busy
        busy = True
        for line in lines[-30:]:
            if "wysłał prośbe o teleportacje" in line:
                if line in last_request:
                    busy = False
                    return
                if not line in last_request:
                    last_request.clear()
                get_random_sound("request_sound", 0.50)
                last_request.append(line)

        busy = False
    while True:
        time.sleep(1)
        if busy == False:
            with open(logs_Path,"r",encoding="utf-8")as f:
                lines = f.readlines()
                check_requests()

def stats():
    tpaccept_quanity = tpaccepts(logs_Path)
    types_quantity = writes_quantity

    print(f"Zaakceptowałeś liczbe {tpaccept_quanity} osób")
    print(f"Napisałeś {types_quantity} razy na chat")

    try:
        print(f"Twoja skuteczność wynosi: {percentages(types_quantity, tpaccept_quanity)}")
    except ZeroDivisionError:
        print("Statystyki nie mogą wynosić 0")

# tworzy tabelke
def tablemaker(day, week_days, percents, start_hour, end_hour, write_time, writes_amount, people_accepted):
    table.add_row([day, week_days, start_hour, end_hour, write_time, percents, writes_amount, people_accepted])
    return table

#zapisuje tabele z danymi
def save(path, save_table):
    with open(path, "a", encoding="utf-8") as file:
        file.write("\n")
        file.write(str(save_table))


def get_writng_time():
    #daje przyblizony czas pisania
  writes_time = writes_quantity * 6.5
  writes_time = writes_time / 60
  writes_time = round(writes_time,1)

  return f"{writes_time}min"
###########################   JSON   ##############################


# ===================== KOMENDY =====================
#ustawia minutnik

def commands_handler():
    while True:
        user_input = input()

        if user_input == "!help":
            print(
                "Zastosowania komend: !stats zbiera informacje z ostatniego "
                "logu gry i wyswietla statystyki"
                "!countdown ustawia minutnik"
            )




# ===================== ZAPIS PRZY ZAMYKANIU =====================
start_hours = current_date(False) # godzina startu
days = current_date(True) # dzisiejsza data
atexit.register(
    lambda: save(
        txt_path,
        tablemaker(
            day = days,
            start_hour = start_hours,
            end_hour = current_date(False),
            percents = percentages(tpaccepts(logs_Path),writes_quantity),
            write_time = get_writng_time(),
            writes_amount=writes_quantity,
            people_accepted= tpaccepts(logs_Path),
            week_days= week_day()
        )
    )
)


# ===================== START PROGRAMU =====================

user_text = load_json()["text"]
user_button = load_json()["chat_key"]

print("dc - Av3nix")
print(f"Nacisnij {load_json()["key_to_start"]} aby odpalic")
print(f"Nacisnij {load_json()["key_to_stop"]} aby zastopowac")
print("dostepne komendy - !help")

keyboard.add_hotkey(load_json()["key_to_start"], program_start) #start
keyboard.add_hotkey(load_json()["key_to_stop"], program_stop) #stop

tpa_checker = threading.Thread(target=got_request)
tpa_checker.start()

commands = threading.Thread(target=commands_handler) # odpala petle z komendami
commands.start()

# ===================== PĘTLA GŁÓWNA =====================
while True:
    if start:
        for i in range(2):
            if start == False:
                break

            if i == 0:
                write_to_chat(user_button, user_text)
                writes_quantity += 1
                wait()

            elif i == 1:
                write_to_chat(user_button, user_text + " " + "!")
                writes_quantity += 1
                wait()
    else:
        time.sleep(0.2)
