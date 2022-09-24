import pygame
from myGametools import mySprite


class Button(mySprite.MyMoveSprite):
    LEISURE = 0
    ON_COVER = 1
    ON_CLICK = 2
    # 不可点击
    DEAD = 3
    def __init__(self,
                 frame,
                 audio,
                 position,
                 speed=None,
                 accelerate=None,
                 dead = False):
        super().__init__(frame, position, speed, accelerate)
        self.audio = audio
        self.clicked = False
        self.covered = False
        self.haveclicked = False
        self.__origin_dead = dead
        self.dead = dead

    def ifonclick(self):
        mousepress = pygame.mouse.get_pressed()
        mousepos   = pygame.mouse.get_pos()
        if mousepress[0]:
            return pygame.Rect.collidepoint(self.rect, mousepos)
        else:
            return False

    def ifoncovered(self):
        mousepos = pygame.mouse.get_pos()
        return pygame.Rect.collidepoint(self.rect, mousepos)

    def onclick(self):
        if not self.dead:
            if not self.clicked:
                if self.ifonclick():
                    self.frame.set_certain(0, self.ON_CLICK, True)
                    self.clicked = True
                    self.audio.downplay()
            elif self.frame.sticked and not self.haveclicked:
                self.haveclicked = True

    def oncover(self):
        if not self.dead:
            if not self.clicked:
                if self.ifoncovered():
                    if not self.covered:
                        self.frame.set_certain(0, self.ON_COVER)
                        self.covered = True
                        self.audio.onplay()
                elif self.covered:
                    self.frame.set_certain(0, self.LEISURE)
                    self.covered = False

    def update(self):
        self.onclick()
        self.oncover()
        super().update()

    def recover(self):
        self.frame.set_certain(0, self.DEAD if self.__origin_dead else self.LEISURE, False)
        self.clicked = False
        self.haveclicked = False
        self.covered = False
