import pygame
class Button:
    def __init__(self,x,y,image,sc_value):
        self.x = x
        self.y = y
        self.img = pygame.image.load(image).convert_alpha()

        prawdziwe_wymiary = self.img.get_bounding_rect()
        self.img = self.img.subsurface(prawdziwe_wymiary)

        self.sc_value = sc_value
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.image = pygame.transform.scale(self.img, (int(sc_value * self.width),int( sc_value * self.height)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.clicked = False
    def draw(self,w):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        w.blit(self.image,(self.rect.x , self.rect.y))
        return action