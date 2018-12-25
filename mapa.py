import pygame
pygame.init()
from random import randint
class Mapa():
    bron = pygame.image.load("sprites/bron.jpg")
    grass = pygame.image.load("sprites/grass.jpg")
    brick = pygame.image.load("sprites/brick.jpg")
    scoreboard = pygame.image.load("sprites/scoreboard.png")
    brick_hor = pygame.image.load("sprites/brick_hor.png")
    brick_ver = pygame.image.load("sprites/brick_ver.png")
    brick_brown = pygame.image.load("sprites/brick_brown.png")
    door_in_wall = pygame.image.load("sprites/door_in_wall.png")
    corner = pygame.image.load("sprites/corner.png")    
    width_map = 17
    height_map = 14
    aray_map =[]
    def __init__(self, width_map, height_map):
        self.width_map = width_map
        self.height_map = height_map
    def create_map(self):
        height_map = self.height_map
        width_map = self.width_map
        aray_map = [ ["0" for h in range( height_map ) ] for w in range( width_map ) ]

        aray_map[0][0] = "scoreboard"
        x = 2
        while x < width_map-2:
            aray_map[x][1] = "brick_hor"
            aray_map[x][height_map-1] = "rev_brick_hor"    
            x +=1
        y = 1
        while y < height_map:
            aray_map[0][y] = "brick_brown"
            aray_map[width_map-1][y] = "rev_brick_brown"
            if y%5==0:
                aray_map[1][y] = "door_in_wall"
                aray_map[width_map-2][y] = "rev_door_in_wall"
            else:
                aray_map[1][y] = "brick_ver"
                aray_map[width_map-2][y] = "rev_brick_ver"    
            y +=1
        aray_map[1][1] = "corner_left_up"
        aray_map[width_map-2][1] = "corner_right_up" 
        aray_map[width_map-2][height_map-1] = "corner_right_down"
        aray_map[1][height_map-1] = "corner_left_down"

        x=2
        y=2
        while x < width_map-2:
            while y < height_map-1:
                if x%2==1 and y%2==1:
                    aray_map[x][y] = "bron"
                else:
                    aray_map[x][y] = "grass"
                y+=1
            y = 2
            x +=1 
        self.aray_map = aray_map
        return aray_map
    def create_brick(self):
        width_map = self.width_map
        height_map = self.height_map
        count_brick = ((width_map - 5)/2 * (height_map - 4)/2) #arithmetic calculation for count brick
        game_map = self.create_map()
        bricks = 0        
        while bricks<=count_brick:
            x = randint(3, width_map-1)
            y = randint(3, height_map-1)
            if game_map[x][y]=="grass":
                game_map[x][y] = "brick"
                bricks += 1
        self.aray_map = game_map
        return game_map
 
    def slash_x(self, x):
        if x % 100 < 35:
            return -1
        if x % 100 > 65:
            return 1
    def slash_y(self, y):
        y = y+25
        if y % 100 < 35:
            return -2
        if y % 100 > 65:
            return 2
    def can_move_point(self, x, y):
        i = int(x/50)
        j = int((y+25)/50)
        if i<0 or j<0 or i>=self.width_map or j>=self.height_map:
            return False
        elif self.aray_map[i][j] == "grass":
            return True
        else:
            return False
    
    def can_move(self, x, y, w = 48, h = 48):
        #return self.can_move_point(x, y) and self.can_move_point(x + w, y) and self.can_move_point(x, y + h) and self.can_move_point(x + w, y + h)
        return self.can_move_point(x+2, y+2) and self.can_move_point(x + w, y+2) and self.can_move_point(x+2, y + h) and self.can_move_point(x + w, y + h)
    def draw_map(self, win):
        game_map = self.aray_map
        i=0
        j=0
        win.blit(self.scoreboard, (0, 0))
        while i < self.width_map:
            while j < self.height_map:
                if game_map[i][j] == "bron":
                    win.blit(self.bron, (50*i, 50*j))
                elif game_map[i][j] == "grass":
                    win.blit(self.grass, (50*i, 50*j))
                elif game_map[i][j] == "brick":
                    win.blit(self.brick, (50*i, 50*j))
                elif game_map[i][j] == "brick_hor":
                    win.blit(self.brick_hor, (50*i, 50*j))
                elif game_map[i][j] == "rev_brick_hor":
                    win.blit(pygame.transform.rotate(self.brick_hor, 180), (50*i, 50*j))
                elif game_map[i][j] == "brick_ver":
                    win.blit(self.brick_ver, (50*i, 50*j))
                elif game_map[i][j] == "rev_brick_ver":
                    win.blit(pygame.transform.rotate(self.brick_ver, 180), (50*i, 50*j))
                elif game_map[i][j] == "brick_brown":
                    win.blit(self.brick_brown, (50*i, 50*j))
                elif game_map[i][j] == "rev_brick_brown":
                    win.blit(pygame.transform.rotate(self.brick_brown, 180), (50*i, 50*j))
                elif game_map[i][j] == "door_in_wall":  
                    win.blit(self.door_in_wall, (50*i, 50*j))
                elif game_map[i][j] == "rev_door_in_wall":  
                    win.blit(pygame.transform.rotate(self.door_in_wall, 180), (50*i, 50*j))
                elif game_map[i][j] == "corner_left_up":
                    win.blit(self.corner, (50*i, 50*j))            
                elif game_map[i][j] == "corner_left_down":
                    win.blit(pygame.transform.flip(self.corner, 0, 1), (50*i, 50*j)) 
                elif game_map[i][j] == "corner_right_down":
                    win.blit(pygame.transform.rotate(self.corner,180), (50*i, 50*j)) 
                elif game_map[i][j] == "corner_right_up":
                    #win.blit(pygame.transform.rotate(self.corner,270), (50*i, 50*j)) 
                    win.blit(pygame.transform.flip(self.corner, 1, 0), (50*i, 50*j))
                #else:
                    #pygame.draw.rect(win, (255,255,0), (i*50, j*50, 50, 50))
                j+=1
            j = 0
            i +=1   
m = Mapa(17,14)
m.create_brick()