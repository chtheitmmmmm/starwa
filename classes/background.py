import pygame
from myGametools import mySprite
from myGametools import mypoint

class BackGround(mySprite.MyMoveSprite):
    def draw(self, screen:pygame.Surface):
        screen.blit(self.frame.image, self.rect)
        self.update()

class UnStopBG(BackGround):
    def __init__(self, frame, position:mypoint.Mypoint, speed=0, accelerate=0):
        self.frame  = frame
        self.rect   = pygame.Rect(*position.position, *self.frame.image.get_size())
        self.speed  = speed
        self.accelerate = accelerate

class LevelUSBG(UnStopBG):
    def draw(self, screen:pygame.Surface):
        lastrect = self.rect
        for i in range(screen.get_width()//self.rect.width + 1):
            screen.blit(self.frame.image, lastrect)
            lastrect.topleft = lastrect.topright
        if self.speed > 0:
            if 0 < self.rect.left < self.rect.width:
                screen.blit(self.frame.image, (self.rect.left-self.rect.width, self.rect.top))
            elif self.rect.left >= self.rect.width:
                self.rect.left = 0
        elif self.speed < 0:
            if lastrect.left <= screen.get_width():
                screen.blit(self.frame.image, lastrect)
            if self.rect.right <= 0:
                self.rect.left = 0
        else:
            return
        self.rect = self.rect.move(self.speed, 0)
        self.speed += self.accelerate

class VerticalUSBG(UnStopBG):
    def draw(self, screen: pygame.Surface):
        lastrect = self.rect.copy()
        for i in range(screen.get_height() // self.rect.height + 1):
            screen.blit(self.frame.image, lastrect)
            lastrect.topleft = lastrect.bottomleft
        if self.speed > 0:
            if 0 < self.rect.top < self.rect.height:
                screen.blit(self.frame.image, (self.rect.left, self.rect.top-self.rect.height, self.rect.width, self.rect.height))
            elif self.rect.top >= self.rect.height:
                self.rect.top = 0
        elif self.speed < 0:
            if lastrect.bottom <= screen.get_height():
                screen.blit(self.frame.image, lastrect)
            if self.rect.bottom <= 0:
                self.rect.top = 0
        else:
            return

        self.rect = self.rect.move(0, self.speed)
        self.speed += self.accelerate







