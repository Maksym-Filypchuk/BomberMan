import pygame
pygame.init()
from mapa import Mapa
from player import Player


win = pygame.display.set_mode((850, 700))
pygame.display.set_caption("Bomberman")
clock = pygame.time.Clock()

mapa = Mapa(17, 14)
game_map = mapa.create_map()

player = Player(win, mapa)

playing = True
while playing:
    #pygame.time.delay(100)
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False   
    mapa.draw_map(game_map, win)
    keys = pygame.key.get_pressed()   
    player.move(keys)
    pygame.display.update()
pygame.quit()