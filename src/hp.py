import pygame
from esign import *
from pygame.sprite import Group

class HpBar(Group):
    def __init__(self, hpCmedia: Media, hpFmedia: Media):
        self.hpc = Item(
            media   = hpCmedia,
            pos     = Vector2(0, 0)
        )
        self.hpf = Item(
            media   = hpFmedia,
            pos     = Vector2(0, 0)
        )

    def configure(self, pos: Vector2, item: HpItem, relative=True):
        """
        与一个 Item 位置绑定
        """
        self.owner      = item
        self.pos        = pos
        self.relative   = relative
        self.hpc.pos    = self.gethpcpos()
        midalign(self.hpc, self.hpf, STICKS1)

    def switchRelativity(self):
        self.relative = not self.relative

    def gethpcpos(self):
        if self.relative:
            return self.pos + Vector2(*self.owner.rect.topleft)
        else:
            return self.pos

    def update(self):
        """
        让PlaneGroup来管理生命值和血条的关系
        """
        # 是否configure
        self.owner
        self.hpc.pos = self.gethpcpos()
        midalign(self.hpc, self.hpf, STICKS1)

    def draw(self, surface: Surface):
        surface.blit(
            pygame.Surface.subsurface(
                self.hpc.image,
                0, 0,
                self.owner.hp.left / self.owner.hp.total * self.hpc.rect.width,
                int(self.hpc.rect.height)
            ),
            (self.hpc.pos.x, self.hpc.pos.y))
        self.hpf.draw(surface)


    def copy(self):
        """
        need configure
        """
        return HpBar(self.hpc.copy(), self.hpf.copy())