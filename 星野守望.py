#
# Created by 程闽 on 2022/01/28
#
'''
因为我害怕失败，所以我不断追求，以变得更强
直面自己的软弱，要有一颗强大的内心，相信自己：加油，你可以的
'''
import pygame, sys
from pygame.locals import *
from init import constants

pygame.init()
pygame.mixer.init(buffer=512)
pygame.mixer.set_num_channels(128)
screen = pygame.display.set_mode(constants.SCREEN_SIZE)

from init import audioInit, globalsInit

globalsInit.convert_screen_init(screen)
pygame.display.set_caption("星际大战 " + constants.version)
pygame.display.set_icon(pygame.image.load('favicon.ico'))
t = pygame.time.Clock()
audioInit.menubgm.play(loops=-1)
while True:
    t.tick(constants.FPS)
    for i in pygame.event.get():
        if i.type == QUIT:
            sys.exit()
    if not globalsInit.flags[globalsInit.GAMEBGING]:
        globalsInit.menu.draw(screen)
        screen.blit(globalsInit.logo.image, globalsInit.logo.rect)
        globalsInit.menu_buttons.draw(screen)
        globalsInit.menu_buttons.update()
        globalsInit.menu.update()
        if globalsInit.bebu.haveclicked:
            globalsInit.flags[globalsInit.GAMEBGING] = True
            audioInit.menubgm.stop()
            audioInit.gamebgm.play(fade_ms=int(audioInit.readygos.get_length()))
    else:
        globalsInit.battlemap1.draw(screen)
        globalsInit.Enemygroup.draw(screen)
        globalsInit.Enemygroup.update(globalsInit.PlayeR)
        globalsInit.PlayeR.update(globalsInit.Enemygroup)
        globalsInit.PlayeR.draw(screen)
        if audioInit.gamebgm.get_num_channels() < 1:
            audioInit.gamebgm.play()
    pygame.display.update()