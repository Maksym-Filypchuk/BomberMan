from mapa import Mapa
import pygame
pygame.init()

win = pygame.display.set_mode((850, 700))
pygame.display.set_caption("Bomberman")

mapa = Mapa(11, 12)
game_map = mapa.create_map()


playing = True
while playing:
    pygame.time.delay(2000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    mapa.draw_map(game_map, win)
    pygame.display.update()
pygame.quit()