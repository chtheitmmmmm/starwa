import random

from myGametools import mySprite, mypoint
from classes.media.frame import frame
from classes.media.audio import plane_audio
from classes.planes.parture import hp
from classes.planes.parture.weapon import gun
from .. import plane


class Sa_1(plane.Plane):
    # destory协议
    DESTORY = 1
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hp.configure(self)
    def update(self):
        super().update()
        if self.destoryed:
            self.havedestoryed = self.frame.sticked

    def draw(self, screen):
        if not self.havedestoryed:
            screen.blit(self.frame.image, self.rect)
            self.hp.draw(screen)
        self.weapon.draw(screen)

    def copy(self, randLoc):
        res = Sa_1(self.name,
                    self.frame.copy(),
                    mypoint.Mypoint(self.rect.topleft),
                    self.audio,
                    self.controlcenter.copy(),
                    self.weapon.copy(),
                    self.hp.copy(),
                    *self.weapon.relative_pos)
        if randLoc:
            left = self.controlcenter.space_b.left
            right = self.controlcenter.space_b.right - self.rect.width
            w = right - left
            top = self.controlcenter.space_b.top
            bottom = self.controlcenter.space_b.bottom - self.rect.height
            h = bottom - top
            res.position = (left + random.random() * w, top + random.random() * h)
            res.hp.configure(res)

        return res