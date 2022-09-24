import pygame
from myGametools import mySprite, mypoint
from classes.media.frame import frame


class Hp:
    def __init__(self, value):
        self.left = value
        self.maxvalue = value

    def lose(self, num):
        if self.left > 0:
            self.left -= num
        if self.left > 0:
            return True
        else:
            self.left = 0

    def get(self, num):
        self.left += num
        if self.left > self.maxvalue:
            self.left = self.maxvalue

    def increase(self, num, getnum=0):
        self.maxvalue += num
        self.get(getnum)

    def decrease(self, num, losenum=0):
        self.maxvalue -= num
        self.lose(losenum)
        self.get(0)

    def copy(self):
        return Hp(self.maxvalue)

class HpBarSprite(mySprite.MyMoveSprite):
    def __init__(self, hp:Hp, frame: frame.Frame, position:mypoint.Mypoint, speed=None, accelerate=None):
        super().__init__(frame, position, speed, accelerate)
        self.hp = hp
        self.totalwidth = self.rect.width
        self.totalimage = self.image
    def update(self):
        self.image = pygame.Surface.subsurface(self.totalimage,
                    (self.totalimage.get_rect().left, self.totalimage.get_rect().top),
                                               (self.hp.left / self.hp.maxvalue * self.totalwidth, self.rect.height))

    def copy(self):
        return HpBarSprite(self.hp.copy(), self.frame.copy(), mypoint.Mypoint(self.rect.topleft), self.speed, self.accelerate)

class HpFrameBar:
    # 将条和框组成一个群组
    def __init__(self, hpbar:HpBarSprite, hpframe:mySprite.MyMoveSprite):
        self.hpbar = hpbar
        self.hpframe = hpframe
    def draw(self, screen):
        screen.blit(self.hpbar.image, self.hpbar.rect)
        screen.blit(self.hpframe.image, self.hpframe.rect)
    def update(self):
        self.hpframe.update()
        self.hpbar.update()
    def __getcenter(self):
        return self.hpbar.rect.center
    def __setcenter(self, other):
        self.hpbar.rect.center = other
        self.hpframe.rect.center = other
    center = property(__getcenter, __setcenter)

    def copy(self):
        return HpFrameBar(self.hpbar.copy(), self.hpframe.copy())

class Enemy_HpFrameBar(HpFrameBar):
    def configure(self, plane):
        self.plane = plane
        self.update()
    def update(self):
        self.hpbar.update()
        self.hpframe.update()
        self.center = (
            self.plane.rect.centerx,
            self.plane.rect.centery-(self.plane.rect.height+self.hpframe.rect.height)//2
        )
    def copy(self):
        return Enemy_HpFrameBar(self.hpbar.copy(), self.hpframe.copy())
    def draw(self, screen):
        super(Enemy_HpFrameBar, self).draw(screen)




