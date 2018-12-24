import pygame
pygame.init()
from mapa import Mapa

class Player():
    win = pygame.display.set_mode((850, 700))
    right = False
    left = False
    up = False
    down = False
    x = 100
    y = 75
    speed=5
    anim_count = 0
    mapa = Mapa(17, 14)
    player_img_stay = [pygame.image.load("sprites/player/stay_1.png"),
    pygame.image.load("sprites/player/stay_2.png"), pygame.image.load("sprites/player/stay_1.png")]

    player_img_down = [pygame.image.load("sprites/player/down_1.png"),
    pygame.image.load("sprites/player/down_2.png"), pygame.image.load("sprites/player/down_3.png")]
    
    player_img_left = [pygame.image.load("sprites/player/left_1.png"),
    pygame.image.load("sprites/player/left_2.png"), pygame.image.load("sprites/player/left_3.png")]
    
    player_img_right = [pygame.image.load("sprites/player/right_1.png"),
    pygame.image.load("sprites/player/right_2.png"), pygame.image.load("sprites/player/right_3.png")]
    
    player_img_up = [pygame.image.load("sprites/player/up_1.png"),
    pygame.image.load("sprites/player/up_2.png"), pygame.image.load("sprites/player/up_3.png")]
    

    def __init__(self, win, mapa):
        self.win = win
        self.mapa = mapa
    def draw_player(self, move):
        if self.anim_count + 1 == 15:
            self.anim_count = 0
        self.win.blit(move[self.anim_count//5], (self.x, self.y))
        #pygame.draw.rect(self.win, (255,255,135), (self.x, self.y, 50,50) )
        self.anim_count += 1

    def when_do_i_walk(self, walk):
        if walk == "left":
            self.right = False
            self.left = True
            self.up = False
            self.down = False
        elif walk == "right":
            self.right = True
            self.left = False
            self.up = False
            self.down = False
        elif walk == "up":
            self.right = False
            self.left = False
            self.up = True
            self.down = False
        elif walk == "down":
            self.right = False
            self.left = False
            self.up = False
            self.down = True
        elif walk == "stay":
            self.right = False
            self.left = False
            self.up = False
            self.down = False

    def move(self, keys):
        if keys[pygame.K_d] and not(self.left) and not(self.up) and not(self.down):
            if self.mapa.can_move(self.x + self.speed, self.y):
                self.x += self.speed
            elif self.mapa.slash_y(self.y) == 2:
                self.y += 1
            elif self.mapa.slash_y(self.y) == -2:
                self.y -= 1
            self.when_do_i_walk("right")
            self.draw_player(self.player_img_right)
        elif keys[pygame.K_a] and not(self.right) and not(self.up) and not(self.down):
            if self.mapa.can_move(self.x - self.speed, self.y):
                self.x -= self.speed
            elif self.mapa.slash_y(self.y) == 2:
                self.y += 1
            elif self.mapa.slash_y(self.y) == -2:
                self.y -= 1
            self.when_do_i_walk("left")
            self.draw_player(self.player_img_left)
        elif keys[pygame.K_w] and not(self.right) and not(self.left) and not(self.down):
            if self.mapa.can_move(self.x, self.y - self.speed):
                self.y -= self.speed
            elif self.mapa.slash_x(self.x) == 1:
                self.x += 1
            elif self.mapa.slash_x(self.x) == -1:
                self.x -= 1
            self.when_do_i_walk("up")
            self.draw_player(self.player_img_up)
        elif keys[pygame.K_s]  and not(self.right) and not(self.left) and not(self.up):
            if self.mapa.can_move(self.x, self.y + self.speed):    
                self.y += self.speed
            elif self.mapa.slash_x(self.x) == 1:
                self.x += 1
            elif self.mapa.slash_x(self.x) == -1:
                self.x -= 1
            self.when_do_i_walk("down")
            self.draw_player(self.player_img_down)
        else:
            self.draw_player(self.player_img_stay)
            self.when_do_i_walk("stay")
            
