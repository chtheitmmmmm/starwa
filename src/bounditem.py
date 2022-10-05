from esign import *
from src.boundlrtb import Boundlftb
from src.bound import BoundUnit

class BoundItem(MovableItem):
    """
    限制自身的速度范围和空间范围
    """
    _selfbound = None
    _speedbound = None
    """
    所有的 bound 在子类中编写，供所有该类的对象共用
    selfbound 设计为用于限制center的位置
    """
    def speedbound(self):
        if not self._speedbound.leftlimit(self.speed.x):
            self.speed.x = self._speedbound.left
        elif not self._speedbound.rightlimit(self.speed.x):
            self.speed.x = self._speedbound.right
        if not self._speedbound.bottomlimit(self.speed.y):
            self.speed.y = self._speedbound.bottom

        elif not self._speedbound.toplimit(self.speed.y):
            self.speed.y = self._speedbound.top

    def selfbound(self):
        if not self._selfbound.leftlimit(self.rect.centerx):
            self.rect.centerx = self._selfbound.left
        elif not self._selfbound.rightlimit(self.rect.centerx):
            self.rect.centerx = self._selfbound.right
        if not self._selfbound.bottomlimit(self.rect.centery):
            self.rect.centery = self._selfbound.bottom
        elif not self._selfbound.toplimit(self.rect.centery):
            self.rect.centery = self._selfbound.top

    def update(self) -> bool:
        self.speedbound()
        self.selfbound()
        return super(BoundItem, self).update()
