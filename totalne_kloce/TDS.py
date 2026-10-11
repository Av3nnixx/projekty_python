from random import randint

import random
dps_list = ["Gold miniguner","Miniguner","Turret","Ranger","Gatling gunner","Enginner","Accelelator","Necromater","Commando","Swarmer","Elementalist","Harvester","Warlock"]
support_list = ["Pyrkoman","Farm","Commander","Medic","DJ,""Mercany Base","Gold pyrko","Fireworker","Archer","Hacker"]
stun_list = ["Electro","Freezer","Warden","Hammer guy","Frost walker","Toxic gunner","Jester","Cyromancer"]
early_list = ["Rocketer","Trapper","Gladiator","Golden Soldier","Golden cowboy","Ace pilot","Soldier","Shotgunner","Assasin","Militiant","Demomen","Hunter","Scout","Sniper","Military base","Golden Scout","Golden Croock Boss","Crook boss","Brawler","Mortar","Paintballer","Cowboy","Slasher","Snowballer","Executioner","Elf Camp","Hallow punk","Biologist"]
dps_index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
support_index = [1, 2, 3, 4, 5, 6, 7, 8, 9]
stun_index = [1, 2, 3, 4, 5, 6, 7, 8]
early_index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
def zipping(index,lista,typ):

    if typ == "dps":
        typ = zip(index, lista)
        typ = dict(typ)
        table = []
        for i in range(2):
            if i == 1:
                while postac == table[0]:
                    los_ind = randint(1, len(typ))
                    postac = typ[los_ind]
                print(postac)
            else:
                los_ind = randint(1, len(typ))
                postac = typ[los_ind]
                print(postac)
                table.append(postac)
    else:
        typ = zip(index, lista)
        typ = dict(typ)
        los_ind = randint(1, len(typ))
        postac = typ[los_ind]
        print(postac)
zipping(dps_index,dps_list,"dps")
zipping(support_index,support_list,"support")
zipping(stun_index,stun_list,"stun")
zipping(early_index,early_list,"early")
