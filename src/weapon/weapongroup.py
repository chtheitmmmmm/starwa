from esign import *
from src.weapon import *

@stateDefine('UNCONFIGURED', 'CONFIGURED')
class WeaponGroup(list):
    """
    Weapon 群，AramedPlane用它管理所有Weapon
    """
    def __init__(self, weapon_relas: list):
        assert all(map(lambda w: isinstance(w, Weapon), (w for w, r in weapon_relas))), "Weapon expected!"
        super().__init__(weapon_relas)
        self.switch('UNCONFIGURED')

    def configure(self, plane):
        self.__plane = plane
        for w, r in self:
            w.configure(plane, r)

    def draw(self, screen: Surface):
        for weapon, r in self:
            weapon.draw(screen)

    def fire(self):
        for weapon, r in self:
            weapon.fire()

    def update(self, aim_group):
        for weapon, r in self:
            weapon.update(aim_group)

    def copy(self):
        """
        返回一个没有配置的武器群
        """
        cp = []
        for w, r in self:
            cp.append((w.copy(), r.copy()))
        return WeaponGroup(cp)

__all__ = ['WeaponGroup']