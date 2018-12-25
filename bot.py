import pygame
pygame.init()
from random import randint
from mapa import Mapa
class Bot():
    win = pygame.display.set_mode((0, 0))
    mapa = Mapa(0, 0)
    
    when_do_i_walk = randint(1, 4)
    how_far = randint(1, 5)
    conter_move = 0
    life = True
    speed = 5
    x = 0
    y = 0
    w = 0
    h = 0
    mob =[]
    anim_count = 0
    mob1 = [pygame.image.load("sprites/mobs/mob1_1.png"),
    pygame.image.load("sprites/mobs/mob1_2.png"),pygame.image.load("sprites/mobs/mob1_3.png"),
    pygame.image.load("sprites/mobs/mob1_2.png")]
    mob2 = [pygame.image.load("sprites/mobs/mob2_1.png"),
    pygame.image.load("sprites/mobs/mob2_2.png"),pygame.image.load("sprites/mobs/mob2_3.png"),
    pygame.image.load("sprites/mobs/mob2_2.png")]
    mob3 = [pygame.image.load("sprites/mobs/mob3_1.png"),
    pygame.image.load("sprites/mobs/mob3_2.png"),pygame.image.load("sprites/mobs/mob3_3.png"),
    pygame.image.load("sprites/mobs/mob3_2.png")]
    mob4 = [pygame.image.load("sprites/mobs/mob4_1.png"),
    pygame.image.load("sprites/mobs/mob4_2.png"),pygame.image.load("sprites/mobs/mob4_3.png"),
    pygame.image.load("sprites/mobs/mob4_2.png")]

    def __init__(self, win, mapa, w, h, mob):
        self.win = win
        self.mapa = mapa
        self.w = w
        self.h = h 
        if mob == 1:
            self.mob = self.mob1
            self.speed = 2
        elif mob == 2:
            self.mob = self.mob2
            self.speed = 4
        elif mob == 3:
            self.mob = self.mob3
            self.speed = 6
        elif mob == 4:
            self.mob = self.mob4
            self.speed = 8
    def create_bot(self):
        created = False
        while not(created):
            x = randint(3, self.w-1)
            y = randint(3, self.h-1)
            if self.mapa.aray_map[x][y]=="grass":
                self.x = x*50
                self.y = y*50
                created = True
    def draw_bot(self):
        if self.anim_count + 1 == 40:
            self.anim_count = 0
        self.win.blit(self.mob[self.anim_count//10], (self.x, self.y))
        #pygame.draw.rect(self.win, (155,155,135), (self.x, self.y, 50,50) )
        self.anim_count += 1
    def can_move_point(self, x, y):
        i = int(x/50)
        j = int(y/50)       
        if self.mapa.aray_map[i][j] == "grass":
            return True
        else:
            return False
    def can_move(self, x, y, w = 49, h = 49):
        return self.can_move_point(x, y) and self.can_move_point(x + w, y) and self.can_move_point(x, y + h) and self.can_move_point(x + w, y + h)
    def random_move(self, start=1, end=5):
        self.conter_move = 0
        self.when_do_i_walk = randint(1, 4)
        self.how_far = randint(start, end)  
        if self.x % 50 < self.speed:
            self.x = int(self.x/50)*50
        elif self.x % 50 > 50 - self.speed:
            self.x = (int(self.x/50)+1)*50
        if self.y % 50 <self.speed:
            self.y = int(self.y/50)*50
        elif self.y % 50 > 50 - self.speed:
            self.y = (int(self.y/50)+1)*50
    def move_bot(self):
        if self.conter_move <= self.how_far*50:
            self.conter_move += self.speed
            if self.when_do_i_walk == 1:
                if(self.can_move(self.x-self.speed, self.y)):
                    self.x -= self.speed
                else: 
                    self.random_move()
                    print(str(self.x)+"-1-"+str(self.y))               
            elif self.when_do_i_walk == 2:
                if(self.can_move(self.x+self.speed, self.y)):
                    self.x += self.speed
                else: 
                    self.random_move()
                    print(str(self.x)+"-2-"+str(self.y))
            elif self.when_do_i_walk == 3:
                if(self.can_move(self.x, self.y-self.speed)):
                    self.y -= self.speed
                else: 
                    self.random_move()
                    print(str(self.x)+"-3-"+str(self.y))
            elif self.when_do_i_walk == 4:
                if(self.can_move(self.x, self.y+self.speed)):
                    self.y += self.speed
                else: 
                    self.random_move()          
                    print(str(self.x)+"-4-"+str(self.y))  
        else: 
            self.random_move()
            print(str(self.x)+"-5-"+str(self.y))
        self.draw_bot()
    
    

        
                