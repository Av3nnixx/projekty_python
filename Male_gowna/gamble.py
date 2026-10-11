import time
import random

stan_konta = 100
tak = ["Tak", "tak"]
nie = ["Nie", "nie"]
klan = ["Av3nix", "Strus28", "Kastifir44", "Kubikssss321", "Szybonowy2"]

nick = input("Wpisz swój nick: ")

if nick in klan:
    print("Jesteś już w klanie,", nick)
else:
    print("Nie jesteś w klanie,", nick)
    pytanie = input("Czy chcesz dołączyć do klanu? ")

    if pytanie in tak:
        print("Czas na rekrutację, oto kilka pytań:")

        pvp = int(input("Na ile oceniasz swój poziom PvP (1-10): "))
        mikrofon = input("Czy masz sprawny mikrofon (Tak/Nie): ")
        wiek = int(input("Ile masz lat: "))
        exp = int(input("Od ilu lat grasz w Minecrafta: "))

        punkty = 0
        punkty += max(0,min(pvp,10)) *2
        punkty += 10  if mikrofon.lower() == "tak" else 0
        punkty += wiek
        punkty += exp *5
        print("Masz razem",punkty,"punktów")
        if punkty > 50:
            print("Dostałeś się, gratulacje",nick)
            klan.append(nick)
            klan.sort()
            time.sleep(2)
            print("Oto lista komend do których masz dostęp: list,info,pomoc,gamble,kradnij,praca,machine")
            while True:
                time.sleep(3)
                komenda = input("Wpisz komende: ")
                if komenda =="list":
                    print(klan)
                if komenda =="info":
                    print("Twój stan konta to",stan_konta)
                    print("Oto twoje punkty",punkty)
                    print("Oto twój nick",nick)
                if komenda =="pomoc":
                    print("Oto lista komend do których masz dostęp: list,info,pomoc,gamble,kradnij,praca,machine")
                if komenda =="gamble":
                    print("Witaj oto prosta minigra twoim celem jest zdobyć jak najwięcej pieniędzy.", end="  ")
                    time.sleep(3)
                    print("Twój początkowy stan konta to:", stan_konta)
                    print("Oto lista komend:")
                    print("gamble-Możesz potroić swój majątek lub go stracić 50/50")
                    gra_komenda = input("Jeżeli jesteś gotowy wpisz ""start")
                    if gra_komenda =="start:":
                        liczba = random.randint(1,2)
                        if liczba == 1:
                            stan_konta = stan_konta *3
                            print("Wygrałeś!!! Twój stan konta to obecnie",stan_konta)
                        if liczba ==2:
                            stan_konta = 0
                            print("Niestety przegrałes twój stan konta wynosi",stan_konta)
                if komenda == "kradnij":
                    if random.random() <0.5:
                        kradziez = random.randint(1,300)
                        print("Ukradles",kradziez,"pieniędzy")
                        stan_konta += kradziez
                        print("Twój aktualny stan konta wynosi",stan_konta)
                    else:
                        zlapanie = random.randint(1,6)
                        if zlapanie ==1:
                            stan_konta = 0
                            print("Zostałeś złapany straciłeś wszystkie pieniądze")
                if komenda =="machine":
                    symbole = ["🍒", "💎", "🍋", "7️⃣", "🍀"]
                    kwota = int(input("Za ile piniędzy chcesz zagrać:"))
                    stan_konta -= kwota
                    wynik = [random.choice(symbole) for _ in range(3)]
                    print("Wynik", " ".join(wynik))
                    if wynik[0] == wynik[1] == wynik[2]:
                        kwota = kwota * 5
                        print("Wygrałeś", kwota)
                        stan_konta += kwota
                    elif wynik[0] == wynik[1] or wynik[1] == wynik[2] or wynik[2] == wynik[0]:
                        kwota = kwota * 2
                        print("Wygrałes", kwota)
                        stan_konta += kwota
                    else:
                        kwota = 0
                        print("Przegrałes")
















