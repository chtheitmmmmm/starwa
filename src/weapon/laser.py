import pygame

from esign import *
from .hurtitem import HurtItem

class Laser(HurtItem):
    """
    激光，可以同时攻击一条线上的所有敌人，且造成同等伤害
    """
    def score(self, aim: HpItem) -> bool:
        return aim.alive() and pygame.sprite.collide_mask(aim, self)

    def update(self, aim_group: pygame.sprite.AbstractGroup) -> bool:
        if self.state == self.PLAIN:
            if super(Laser, self).update(aim_group):
                self.switch('HITTABLE')
        elif self.state == self.HITTABLE:
            if super(Laser, self).update(aim_group):
                self.switch('DELETABLE')
            