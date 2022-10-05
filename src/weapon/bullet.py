import pygame
from esign import *
from .hurtitem import *
from src.acceitem import AcceItem
@stateDefine('BOOMING')
class Bullet(AcceItem, HurtItem):
    """
    {
        'ord': {
        },
        'boom': {
        }
    }
    """
    collide_ratio = pygame.sprite.collide_circle_ratio(0.5)
    def __init__(self, *args, **kwargs):
        super(Bullet, self).__init__(*args, **kwargs)
        self.switch('HITTABLE')
    
    def score(self, aim: HpItem) -> bool:
        '''
        自身没有爆炸，对象存活，并且在判定范围内
        '''
        return self.state == self.HITTABLE and aim.alive() and self.collide_ratio(self, aim)

    def hit(self, aim: HpItem):
        super(Bullet, self).hit(aim)
        self.switch('BOOMING')
        self.action('boom')
        self.speed = Vector2(0, 0)
        self.accelerate = Vector2(0, 0)
    
    def copy(self):
        return Bullet(
            media = self.media,
            pos   = self.pos,
            hurt  = self.hurt
        )

    def update(self, aim_group: pygame.sprite.Group) -> bool:
        if self.state == self.BOOMING:
            if super(Bullet, self).update(aim_group=aim_group):
                self.switch('DELETABLE')
        elif self.state == self.HITTABLE:
            super(Bullet, self).update(aim_group=aim_group)

    def draw(self, screen: pygame.Surface):
        if self.state != self.DELETABLE:
            super(Bullet, self).draw(screen)
__all__ = ['Bullet']



