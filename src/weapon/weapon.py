import threading
import time

from .hurtitem import *
from esign import *
from src.weapon import *
from src.constants import constants
from src.boundlrtb import *
fps = constants['meta']['FPS']

windowlimit = Boundlftb.From(
    Vector2(0, constants['meta']['windowSize'][0]),
    Vector2(0, constants['meta']['windowSize'][1])
)

@stateDefine('CONFIGURED', 'UNCONFIGURED')
class Weapon(pygame.sprite.Group):
    """
    武器有两种状态：配置好了和没有配置
    """
    def __init__(self, output: HurtItem):
        super(Weapon, self).__init__()
        self.switch('UNCONFIGURED')
        self.__output = output

    def configure(self, owner, relative: Vector2):
        assert isinstance(relative, Vector2), 'Vector2 expected!'
        self.__owner = owner
        self.__relative = relative
        self.switch('CONFIGURED')

    @property
    def output(self):
        return self.__output

    @property
    def owner(self):
        return self.__owner

    @property
    def relative(self):
        return self.__relative

    def load(self) -> bool:
        """
        此函数返回值用于判断是否调用 addoutput
        """
        return True

    def fire(self):
        self.add(HurtItem(
            self.output.media,
            Vector2(
                self.owner.rect.left + self.owner.rect.width * self.relative[0] - self.output.rect.width / 2,
                self.owner.rect.top + self.relative[1]
            ),
            self.output.hurt
        ))

    def update(self, aim_group: pygame.sprite.AbstractGroup):
        for o in self.sprites():
            if o.state == o.DELETABLE:
                self.remove(o)
            else:
                o.update(aim_group)

    def copy(self):
        return Weapon(self.__output)


@stateDefine(
    'PENDDING',  # 表示正在等待射击指令
    'SHOOTING'  # 表示正在射击，不允许发送射击指令
)
class ConstantBulletGun(Weapon):
    """
    为发射提供控制，防止用户疯狂发射
    """

    def __init__(self, bullet: Bullet):
        super(ConstantBulletGun, self).__init__(bullet)
        self.__internal = self.output.rect.height / self.output.speed.length

    @property
    def internal(self):
        return self.__internal

    def configure(self, owner, relative: Vector2):
        super(ConstantBulletGun, self).configure(owner, relative)
        self.switch('PENDDING')

    def addoutput(self):
        b = Bullet(
            media = self.output.media.copy(),
            pos   = Vector2(
                self.owner.rect.left + self.owner.rect.width * self.relative[0] - self.output.rect.width / 2,
                self.owner.rect.top + self.relative[1]
            ),
            speed = self.output.speed.copy(),
            accelerate = self.output.accelerate.copy(),
            hurt  = self.output.hurt
        )
        self.add(b)
        return b

    def fire(self, num):
        """
        首次发射子弹调用
        """
        if self.state == self.PENDDING:
            self.switch('SHOOTING')
            threading.Thread(target=self.__continue_fire, args=(num,)).start()


    def __continue_fire(self, continue_num):
        while continue_num:
            self.addoutput()
            time.sleep(self.internal / fps)
            if self.owner.state != self.owner.PLAIN:
                break
            continue_num -= 1
        self.switch('PENDDING')

    def update(self, aim_group: pygame.sprite.AbstractGroup):
        super(ConstantBulletGun, self).update(aim_group)
        for bullet in self.sprites():
            if not windowlimit.ylimit(bullet.rect.centery):
                bullet.switch("DELETABLE")

    def copy(self):
        return type(self)(self.output)



def firenumfy(num):
    def _firenumfy(cls):
        def newfire(self):
            super(cls, self).fire(num)
        cls.fire = newfire
        return cls
    return _firenumfy

__all__ = ['Weapon', 'ConstantBulletGun', 'firenumfy']