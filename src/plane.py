from src.hp import HpBar
from src.acceitem import *
from src.bounditem import *
from src.constants import constants
from src.bound import BoundUnit
from src.weapon import *


@stateDefine('PLAIN', 'BOOMING', 'BOOMED')
class Plane(AcceItem, BoundItem, HpItem):
    """
    有加速度，有位置、速度限制，有生命值
    初始速度默认写死为0
    {
        'ord':
        'boom'
    }
    """
    LEFT_ACCE           = 0
    RIGHT_ACCE          = 1
    TOP_ACCE            = 2
    BOTTOM_ACCE         = 3
    LEFT_TOP_ACCE       = 4
    LEFT_BOTTOM_ACCE    = 5
    RIGHT_TOP_ACCE      = 6
    RIGHT_BOTTOM_ACCE   = 7
    _selfbound = Boundlftb(
        BoundUnit(0, constants['meta']['windowSize'][0]),
        BoundUnit(0, constants['meta']['windowSize'][1])
    )
    _speedbound = Boundlftb(
        BoundUnit(-20, 20),
        BoundUnit(-20, 10)
    )
    def __init__(
            self,
            *args,
            acce = (0, 0, 0, 0),
            hpbar: HpBar,
            **kwargs
        ):
        """
        传入 media，pos，hp: Hpv, hpBar, acce（四元组：上、下、左、右，均为正数，会自动处理）即可
        media格式：{
            'ord':
            'boom':
        }
        """
        assert isinstance(acce, tuple) and all(isinstance(i, float | int) for i in acce)
        super(Plane, self).__init__(
            *args,
            speed       = Vector2(0, 0),
            accelerate  = Vector2(0, 0),
            **kwargs
        )
        hpbar.configure(Vector2(
            (self.media.image.get_width() - hpbar.hpf.media.image.get_width()) // 2,
            -int(hpbar.hpf.image.get_height() * 0.8)
        ), self)
        hpbar.update()
        self.hpbar = hpbar
        self.__left_acce = Vector2(-acce[2], 0)
        self.__right_acce = Vector2(acce[3], 0)
        self.__top_acce = Vector2(0, -acce[0])
        self.__bottom_acce = Vector2(0, acce[1])
        self.__leftbottom_acce = self.__left_acce + self.__bottom_acce
        self.__lefttop_acce = self.__left_acce + self.__top_acce
        self.__rightbottom_acce = self.__right_acce + self.__bottom_acce
        self.__righttop_acce = self.__right_acce + self.__top_acce
        self.switch('PLAIN')

    def acce(self, direction):
        if direction == self.LEFT_ACCE:
            self.accelerate = self.__left_acce.copy()
        elif direction == self.RIGHT_ACCE:
            self.accelerate = self.__right_acce.copy()
        elif direction == self.TOP_ACCE:
            self.accelerate = self.__top_acce.copy()
        elif direction == self.BOTTOM_ACCE:
            self.accelerate = self.__bottom_acce.copy()
        elif direction == self.LEFT_TOP_ACCE:
            self.accelerate = self.__lefttop_acce.copy()
        elif direction == self.LEFT_BOTTOM_ACCE:
            self.accelerate = self.__leftbottom_acce.copy()
        elif direction == self.RIGHT_TOP_ACCE:
            self.accelerate = self.__righttop_acce.copy()
        elif direction == self.RIGHT_BOTTOM_ACCE:
            self.accelerate = self.__rightbottom_acce.copy()

    def update(self, *args, **kwargs):
        if   self.state == self.PLAIN:
            super(Plane, self).update(*args, **kwargs)
            self.hpbar.update()
            if not self.alive():
                self.switch("BOOMING")
                self.action('boom')
                self.speed = Vector2(0, 0)
                self.accelerate = Vector2(0, 0)
        elif self.state == self.BOOMING:
            if super(Plane, self).update(*args, **kwargs):
                self.switch('BOOMED')

    def draw(self, screen: Surface) -> None:
        super(Plane, self).draw(screen)
        self.hpbar.draw(screen)

    def copy(self):
        return Plane(
            meida = self.media,
            pos   = self.pos
        )

@stateDefine('DELETABLE')
class ArmedPlane(Plane):
    """
    武装的飞机类，拥有武器。
    考虑到可能有的飞机没有武器，故做此安排
    """
    def __init__(self, *args, **kwargs):
        super(ArmedPlane, self).__init__(*args, **kwargs)
        self.weaponState = StateMachine('CONFIGURED', 'UNCONFIGURED')
        self.weaponState.switch('UNCONFIGURED')

    def update(self, enemy_group):
        self.weapons.update(enemy_group)
        if self.state == self.PLAIN:
            super(Plane, self).update()
            self.hpbar.update()
            if not self.alive():
                self.switch("BOOMING")
                self.action('boom')
                self.speed = Vector2(0, 0)
                self.accelerate = Vector2(0, 0)
        elif self.state == self.BOOMING:
            if super(Plane, self).update():
                self.switch('BOOMED')
        elif self.state == self.BOOMED:
            super(Plane, self).update()
            if all(not weapon[0].sprites() for weapon in self.weapons):
                self.switch('DELETABLE')

    def configureWeapon(self, weapons: WeaponGroup):
        """
        *relatives 为武器产生的伤害点实例的中心相对于飞机的位置:
            x值为相对于飞机自身宽度的分数，
            y值为相对于飞机顶部的位置，若为正数则向机尾，负数则向机头
        """
        assert isinstance(weapons, WeaponGroup)
        self.__weapons = weapons
        weapons.configure(self)
        self.weaponState.switch('CONFIGURED')

    @property
    def weapons(self):
        return self.__weapons

    def draw(self, screen: Surface) -> None:
        if self.state != self.BOOMED and self.state != self.DELETABLE:
            super(ArmedPlane, self).draw(screen)
        if self.weaponState.value == 'CONFIGURED':
            self.weapons.draw(screen)

    def fire(self):
        self.weapons.fire()


__all__ = ['Plane', 'ArmedPlane']