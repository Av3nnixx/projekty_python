import os
import sys
import pygame
import button
from random import randint
#w
pygame.init()
window = pygame.display.set_mode((1280,720))
background = pygame.image.load("tlo.png")
pygame.display.set_caption("Menu")
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
class Menu:
    def __init__(self):
        pass
    def draw_text(self,text,font,textcol,x,y):
        img = font.render(text,True,textcol)
        window.blit(img, (x,y))
class Player:
    def __init__(self):
        self.x_cord = 0
        self.y_cord = 0
        self.image = pygame.image.load("boberkurwa.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.speed = 2
        self.hitbox = pygame.Rect(self.x_cord,self.y_cord,self.width,self.height)
        self.plr_mask = pygame.mask.from_surface(self.image)
    def check_borders(self):
        if self.x_cord > 1280 - self.width or self.y_cord > 720 - self.height or self.x_cord < 0 or self.y_cord < 0:
            self.x_cord = (1280 - self.width )/ 2
            self.y_cord = (720 - self.height) / 2
    def tick(self,keys):
        if keys[pygame.K_w]:
            self.y_cord -= self.speed
            pass
        if keys[pygame.K_a]:
            self.x_cord -= self.speed
            pass
        if keys[pygame.K_s]:
            self.y_cord += self.speed
            pass
        if keys[pygame.K_d]:
            self.x_cord += self.speed
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def draw(self):
        window.blit(self.image, (self.x_cord,self.y_cord))


class Trap:
    def __init__(self):
        self.image = pygame.image.load("bobertrap.png").convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self._y_cord = randint(0, 720 )
        self._x_cord = randint(0, 1280 )
        self.image = pygame.transform.scale(self.image, (0.5 * self.width,0.5 * self.height))
        self.hitbox = self.image.get_rect(center=(self._x_cord, self._y_cord))
        self.dmg = 10
        self.score = 0
        self.dmgable = False
        self.timer_active = False
        self.timer_start = 0
        self.delay = 2000 # 2s
        self.ready_to_delete = False
        self.done_change = False
        self.trap_mask = pygame.mask.from_surface(self.image)
        self.spawn_time = pygame.time.get_ticks()
        self.change_delay = randint(5000 , 15000)
    def change_image(self):

        if self.done_change == False :
            self.image = pygame.image.load("cactus.png")
            self.dmgable = True
            self.image = pygame.transform.scale(self.image, (0.5 * self.width, 0.5 * self.height))
            self.trap_mask = pygame.mask.from_surface(self.image)
            self.hitbox = self.image.get_rect(center=(self._x_cord, self._y_cord))
            self.timer_active = True
            self.timer_start = pygame.time.get_ticks()
            self.done_change = True

    def tick(self):
        now = pygame.time.get_ticks()

        if not self.done_change:
            if now - self.spawn_time >= self.change_delay:
                self.change_image()
        if not self.timer_active:
            return
        if now - self.timer_start >= self.delay:
            self.timer_active = False
            self.ready_to_delete = True



    def draw(self):
        window.blit(self.image, self.hitbox)
class Axe:

    def gamble_cords(self):
        side = randint(0, 3)

        if side == 0:  # left
            self._x_cord = 0
            self._y_cord = randint(0, 720)
            self.direction = "Right"

        elif side == 1: #right
            self._x_cord = 1280
            self._y_cord = randint(0, 720)
            self.direction = "Left"

        elif side == 2: #up
            self._x_cord = randint(0, 1280)
            self._y_cord = 0
            self.direction = "Down"

        else:  # down
            self._x_cord = randint(0, 1280 )
            self._y_cord = 720
            self.direction = "Up"

    def __init__(self):
        self.rot_speed = 2
        self.move_speed = 2
        self._x_cord = 0
        self._y_cord = 0
        self.angle = 1
        self.image = pygame.image.load("sikiera.png").convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (0.5 * self.width,0.5 * self.height))
        self.rotated_axe = pygame.transform.rotate(self.image, self.angle)
        self.hitbox = self.rotated_axe.get_rect(center=(self._x_cord, self._y_cord))
        self.direction = ""
        self.axe_mask = pygame.mask.from_surface(self.image)
    @property
    def x_cord(self):
        return self._x_cord

    @property
    def y_cord(self):
        return self._y_cord
    @x_cord.setter
    def x_cord(self,value):
        self._x_cord = value
    @y_cord.setter
    def y_cord(self,value):
        self._y_cord = value
    def move(self):
        if self.direction == "Right":
            self._x_cord += self.move_speed
        if self.direction == "Left":
            self._x_cord -= self.move_speed
        if self.direction == "Down":
            self._y_cord += self.move_speed
        if self.direction ==  "Up":
            self._y_cord -= self.move_speed


    def tick(self):
        self.angle += self.rot_speed
        self.rotated_axe = pygame.transform.rotate(self.image, self.angle)
        self.axe_mask = pygame.mask.from_surface(self.rotated_axe)
        self.hitbox = self.rotated_axe.get_rect(center=(self.x_cord, self.y_cord))
        self.move()
    def draw(self):
        window.blit(self.rotated_axe, self.hitbox)


class HealhBar:
    def __init__(self,x,y,w,h,max_hp):
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp
        self.x = x
        self.y = y
    def draw(self,surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface,"red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface,"green",(self.x,self.y, self.w * ratio,self.h))


class Cash:
    def __init__(self):
        self.x_cord = randint(100,1180)
        self.y_cord = randint(80,620)
        self.image = pygame.image.load("platypek.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        self.cash_mask = pygame.mask.from_surface(self.image)
        self.ready_to_delete = False
    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image,(self.x_cord,self.y_cord))
class Attribute:
    def __init__(self,image_path,sc_value,boost_time):
        self.boost_time= boost_time
        self.y_cord = randint(0, 720)
        self.x_cord = randint(0, 1280)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (sc_value * self.width, sc_value * self.height))
        self.hitbox = self.image.get_rect(
            center=(self.x_cord, self.y_cord)
        )
        self.boosted = False
        self.a_mask = pygame.mask.from_surface(self.image)
        self.boost_clock = 0
        self.ready_to_delete = False
    def tick(self,dt,fnc):
        if self.boosted:
            self.boost_clock += dt
            if self.boost_clock >= self.boost_time:
                fnc()
                self.boost_clock = 0
                self.ready_to_delete = True
    def draw(self):
        if not self.boosted:
            window.blit(self.image,self.hitbox)
    def boost(self,fnc):
        if not self.boosted:
            fnc()
            self.boosted = True

class Drink(Attribute):
    def __init__(self):
        super().__init__("bober energy.png.png", 0.3, 50)
    def give_a_speed(self,plr):
        plr.speed += 0.5
    def normal_speed(self,plr):
        plr.speed -= 0.5
class Barszcz(Attribute):
    def __init__(self):
        super().__init__("barszcz.png", 0.2, None)
    def heal(self,hb):
        if hb.hp < hb.max_hp:
            hb.hp += 10
            if hb.hp < hb.max_hp:
                hb.hp += 10

def main():
    run = True
    game_pause = False
    #objects
    axes = []
    traps = []
    drinks = []
    banknotes = []
    # Instances
    player = Player()
    health_bar = HealhBar(980,0,300,40,100)
    pause_title = Menu()
    start_button = button.Button(640, 230, "menu/resumeButton.png", 0.3)
    settings_button = button.Button(640, 350, "menu/Settings button.png", 0.3)
    quit_button = button.Button(640, 470, "menu/Quit button.png", 0.3)
    pg_button = button.Button(640,350,'play again.png', 0.3)
    #variables
    game_clock = pygame.time.Clock()
    clocks = {"score_food": 0, "axe": 0, "trap": 0,"energy_drink": 0,"barszcz": 0, "trap_despawn": 0}
    score = 0
    pause_title = Menu()
    barszcze = []
    go_screen = pygame.image.load("Game over.png")
    difficulty = 1 + score / 10
    while run:
        #ticks
        dt = game_clock.tick(60) / 100
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # if space pressed
                    print("pause")
                    game_pause = not game_pause
            if event.type == pygame.QUIT:  # if player quit
                run = False
        keys = pygame.key.get_pressed()

        #ui drawing
        score_image = pygame.font.Font.render(pygame.font.SysFont("truneo", 48), f"wynik: {str(score)}", True, (239, 255, 237))
        window.blit(background, (0, 0))
        health_bar.draw(window)
        window.blit(score_image, (10, 10))
        if game_pause == True:
            #if game is paused - no ticks
            for axe in axes:
                axe.draw()
            for banknote in banknotes:
                banknote.draw()
            for drin in drinks:
                drin.draw()
            for trap in traps:
                trap.draw()
            player.draw()
            if start_button.draw(window) == True:
                game_pause = not game_pause
            if quit_button.draw(window) == True:
                run = False
            if settings_button.draw(window) == True:
                print("seetigns")
            pygame.display.update()
            continue
        elif health_bar.hp <= 0:
            #if your ded
            window.blit(go_screen,(0,0))
            pg_button.draw(window)
            pygame.display.update()
            continue
        else:
            pause_title.draw_text("Press SPACE to pause", pygame.font.SysFont("truneo", 24), (255, 255, 0), 1060,40)


        for i,v in clocks.items():
            clocks[i] += dt
            if i == "score_food":
                if clocks[i] > 30:
                    banknotes.append(Cash())
                    clocks[i] = 0
            elif i == "axe":
                if clocks[i] >  (10 / difficulty) + 1:
                    axe = Axe()
                    axe.gamble_cords()
                    axes.append(axe)
                    clocks[i] = 0
            elif i == "trap":
                if clocks[i] > (150 / difficulty) + 50:
                    trap = Trap()
                    traps.append(trap)
                    clocks[i] = 0
            elif i == "energy_drink":
                if clocks[i] > 210:
                    drink = Drink()
                    drinks.append(drink)
                    clocks[i] = 0
            elif i == "barszcz":
                if clocks[i] > 20 + 150 / (1 + score / 50):
                    barszcz = Barszcz()
                    barszcze.append(barszcz)
                    clocks[i] = 0

        #mouse_x, mouse_y = pygame.mouse.get_pos()
        #print(f"Mouse x {mouse_x}, mouse y {mouse_y}")

        for trap in traps:
            trap.draw()
            trap.tick()
            if player.plr_mask.overlap(trap.trap_mask,(trap.hitbox.x - player.hitbox.x, trap.hitbox.y - player.hitbox.y)):
                #zadamoe dmg
                if trap.dmgable:
                    health_bar.hp -= 20
                    trap.ready_to_delete = True
        # po czasie znika ktory jest w funkcji tick
        traps = [trap for trap in traps if not trap.ready_to_delete]

        #banknotes
        for banknote in banknotes:
            banknote.tick()
            banknote.draw()

            if player.plr_mask.overlap(banknote.cash_mask,(banknote.hitbox.x - player.hitbox.x, banknote.hitbox.y - player.hitbox.y)):
                score += 1
                banknote.ready_to_delete = True

        banknotes = [banknote for banknote in banknotes if not banknote.ready_to_delete]
                #zmienie trapa na kaktusa
        #axes
        for axe in axes:
            axe.tick()
            axe.draw()

        for i,axe1 in enumerate(axes):
            #kolizje
            if player.plr_mask.overlap(axe1.axe_mask, (axe1.hitbox.x - player.hitbox.x, axe1.hitbox.y - player.hitbox.y)):
                health_bar.hp -= 10
                axes.remove(axe1)
            # usuniecie gdy wyszlo za ekran
            if axe1.x_cord > 1300 or axe1.y_cord > 800 or axe1.y_cord < 0 or axe1.x_cord < 0:
                axes.pop(i)
                del axe1

        #energy drinks
        for i,drin in enumerate(drinks):
            drin.draw()
            drin.tick(dt,lambda: drin.normal_speed(player))
            if player.plr_mask.overlap(drin.a_mask,(drin.hitbox.x - player.hitbox.x, drin.hitbox.y - player.hitbox.y)):
                drin.boost((lambda : drin.give_a_speed(player)))
        drinks = [drin for drin in drinks if not drin.ready_to_delete]
        for barszcz in barszcze:
            barszcz.draw()
            if player.plr_mask.overlap(barszcz.a_mask,(barszcz.hitbox.x - player.hitbox.x, barszcz.hitbox.y - player.hitbox.y)):
                barszcz.boost(lambda: barszcz.heal(health_bar))
        #player
        player.check_borders()
        player.tick(keys)
        player.draw()

        pygame.display.update()
if __name__ == "__main__":
   main()
