import pygame
from myGametools import mySprite, mypoint


class Bullet(mySprite.MyMoveSprite):
    LEISURE = 0
    BOOMING = 1
    collide_ratio = pygame.sprite.collide_circle_ratio(0.5)
    def __init__(self, hurt, frame, audio, position:mypoint.Mypoint, speed=None, accelerate=None, leisurenumber=LEISURE,):
        super().__init__(frame, position, speed, accelerate)
        self.audio = audio
        self.boomed = False
        self.haveboomed = False
        self.hurt = hurt

    def collide_update(self, aim_group:pygame.sprite.Group | None):
        '''
        remember call this every circle
        :param aim_group:
        :return:
        '''
        if not self.boomed:
            for i in (aim_group if aim_group else []):
                if self.collide_ratio(self, i) and not i.destoryed:
                    self.frame.set_certain(0, self.BOOMING, True)
                    self.boomed = True
                    self.audio.hitplay()
                    self.speed=[0,0]
                    self.accelerate = [0,0]
                    # 遵守hit协议
                    i.hit(self)
        else:
            self.haveboomed = self.frame.sticked
    def copy(self):
        return Bullet(
            self.frame.copy(),
            self.audio,
            mypoint.Mypoint(self.rect.topleft),
            self.speed,
            self.accelerate,
            self.LEISURE)

    def update(self) -> None:
        super().update()
        if self.frame.sticked:
            self.haveboomed = True




