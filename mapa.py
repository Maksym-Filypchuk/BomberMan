import pygame
pygame.init()
class Mapa():
    width_map = 17
    height_map = 14
    def __init__(self, width_map, height_map):
        self.width_map = width_map
        self.height_map = height_map
    def create_map(self):
        height_map = self.height_map
        width_map = self.width_map
        aray_map = [ ["0" for h in range( height_map ) ] for w in range( width_map ) ]
        aray_map[0][0] = "scoreboard"
        aray_map[1][1] = "corner_left_up"
        aray_map[width_map-2][1] = "corner_right_up" 
        aray_map[width_map-2][height_map-1] = "corner_right_down"
        aray_map[1][height_map-1] = "corner_left_down"

        x = 2
        while x < width_map-2:
            aray_map[x][2] = "hor_line"
            aray_map[x][height_map-1] = "hor_line"    
            x +=1
        y = 1
        while y < height_map:
            aray_map[0][y] = "first_ver_line"
            aray_map[width_map-1][y] = "rev_first_ver_line"
            if y%5==0:
                aray_map[1][y] = "door_in_wall"
                aray_map[width_map-2][y] = "rev_door_in_wall"
            else:
                aray_map[1][y] = "second_ver_line"
                aray_map[width_map-2][y] = "rev_second_ver_line"    
            y +=1

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
        return aray_map
    


    def draw_map(self, game_map, win):
        i=0
        j=0
        bron = pygame.image.load("sprites/bron.jpg")
        grass = pygame.image.load("sprites/grass.jpg")
        while i < self.width_map:
            while j < self.height_map:
                if game_map[i][j] == "bron":
                    win.blit(bron, (50*i, 50*j))
                elif game_map[i][j] == "grass":
                    win.blit(grass, (50*i, 50*j))
                else:
                    pygame.draw.rect(win, (255,255,0), (i*50, j*50, 50, 50))
                j+=1
            j = 0
            i +=1   