import os
import asyncio
import random
import time
from dotenv import load_dotenv

load_dotenv(".env")

boss_hp = os.getenv("BOSS_HP")
boss_name: str = os.getenv("BOSS_NAME")
if boss_hp is None or boss_name is None:
    raise ValueError("Brak configu w envirotment")
boss_hp = int(boss_hp)

class Hero:
    def __init__(self,name,hp,dmg,cooldown):
        self.name = name
        self.hp = [hp]
        self.dmg = dmg
        self.cooldown = cooldown
        self.roll = random.randint(1,3)
        self.miss_value = 0
    def __str__(self):
        return f"To jest {self.name}, zadaje {self.dmg}dmg, ma {self.hp}hp a jego szybkosc ataku wynosi {self.cooldown}s"
    async def attack(self,enemy):
        self.miss_value = random.randint(1,3)
        if self.miss_value == self.roll:
            print(f"{self.name} spudłował atak")
        else:
            await asyncio.sleep(self.cooldown)
            enemy.hp[0] -= self.dmg
async def main():
    #env
    # Postacie
    boss = Hero(boss_name,boss_hp,0,0)
    heros = {
    "mag" : Hero("Mag",10,30,10),
    "archer" : Hero("Łucznik",5,5,10),
    "warrior" : Hero("Wojownik",50,60,10),
    }
    # atakowanie
    cooldawns = []
    start = time.time()
    await asyncio.gather(* [hero.attack(boss) for hero in heros.values()])
    end = time.time()
    print(f"Bossowi zostało {boss.hp[0]}, oberwał {boss_hp - boss.hp[0]},{"żyje" if boss.hp[0] > 0 else "nie żyje"} a trwało to {end - start:.2f} sekund ")
asyncio.run(main())



