import pygame
pygame.init()
from mapa import Mapa
from player import Player
from bot import Bot

win = pygame.display.set_mode((850, 700))
pygame.display.set_caption("Bomberman")
clock = pygame.time.Clock()

mapa = Mapa(17, 14)
mapa.create_brick()
player = Player(win, mapa)
bot1 = Bot(win, mapa, 17, 14, 1)
bot2 = Bot(win, mapa, 17, 14, 2)
bot3 = Bot(win, mapa, 17, 14, 3)
bot4 = Bot(win, mapa, 17, 14, 4)
bot1.create_bot()
bot2.create_bot()
bot3.create_bot()
bot4.create_bot()
playing = True
while playing:
    #pygame.time.delay(100)
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False   
    mapa.draw_map(win)
    keys = pygame.key.get_pressed()   
    player.move(keys)
    bot1.move_bot()
    bot2.move_bot()
    bot3.move_bot()
    bot4.move_bot()
    pygame.display.update()
pygame.quit()