import pygame
from .media import *
from .tools import *
from .constants import *

class Item(pygame.sprite.Sprite):
    """
    泛指一切能够在屏幕上渲染出内容的对象
    """
    __slots__ = ['media']

    def __init__(self, *args, media: Media, pos: Vector2, **kwargs):
        super(Item, self).__init__()
        self.media: Media = media
        self.rect = pygame.Rect(pos.x, pos.y, *self.media.image.get_size())

    def __getpos(self) -> Vector2:
        return Vector2(*self.rect.topleft)

    def __setpos(self, pos):
        self.rect.topleft = (pos.x, pos.y)

    pos = property(__getpos, __setpos)

    @property
    def image(self):
        return self.media.image

    @property
    def audio(self):
        return self.media.audio


    def action(self, name: str):
        """
        开始执行某一个动作链
        """
        self.media.switchActionChain(name)

    def update(self, *args, **kwargs) -> bool:
        """
        更新帧
        """
        return self.media.update()

    def draw(self, screen: pygame.Surface):
        """
        绘制在屏幕上
        """
        screen.blit(self.image, self.rect)

    def copy(self):
        return Item(
            media = self.media,
            pos   = self.pos
        )

    def handle(self, e: pygame.event.Event):
        """
        处理事件的钩子
        """
        pass


class MovableItem(Item):
    """
    可以绘制在屏幕上的可以移动的对象，用户可以自己定制有加速度的子类
    """
    __slots__ = ['speed']
    def __init__(
            self,
            *args,
            speed: Vector2 | None=Vector2(0, 0),        # 当设置为 None，表示继承者已经在类中编写了其实例的共有速度
            **kwargs
        ):
        super(MovableItem, self).__init__(*args, **kwargs)
        if speed:
            self.speed = speed.copy()

    def move(self):
        self.pos += self.speed

    def update(self, *args, **kwargs) -> bool:
        self.move()
        return super().update(*args, **kwargs)

    def copy(self):
        return MovableItem(
            media = self.media,
            pos   = self.pos,
            speed = self.speed
        )

class StatefulItem(Item):
    """
    有状态的Item
    """
    def __init__(
            self,
            *args,
            states: StateMachine,
            **kwargs
        ):
        super(StatefulItem, self).__init__(*args, **kwargs)
        self.states = states

    def switchState(self, name: str | int):
        self.states.switch(name)

    def getState(self):
        return self.states.value

class Hpv:
    """
    整数生命值解决方案
    """
    __slots__ = ['__left', '__total']
    def __init__(self, total: int, left: int=-1):
        assert total > 0, "Total hp illegal!"
        assert 0 <= left <= total or left == -1, "Left hp illegal!"
        assert isinstance(total, int) and isinstance(left, int), "Integer expected!"
        if left == -1:
            self.__left = total
        else:
            self.__left = left
        self.__total = total                                  # 总生命值

    @property
    def total(self):
        return self.__total
    @total.setter
    def __settotal(self, newvalue):
        assert self.__left <= newvalue, "Illegal new total hp."

    @property
    def left(self):
        return self.__left

    def lose(self, num: int):
        if self.__left > num:
            self.__left -= num
        else:
            self.__left = 0

    def gain(self, num: int):
        if self.left + num > self.total:
            self.__left = self.total
        else:
            self.__left += num

    def __inrange(self):
        return 0 <= self <= self.total

    @staticmethod
    def _check(fn):
        def check(self, *args, **kwargs):
            r = fn(self, *args, **kwargs)
            if not self.__inrange():
                raise ValueError('Hp illegal!')
            return r
        return check

    def __str__(self):
        return f'Hp[{self.left}]'

    def resume(self):
        """
        resume to full state.
        """
        self.__left = self.total

    def clear(self):
        self.__left = 0

    def copy(self):
        return Hpv(self.total, self.__left)

class HpItem(Item):
    """
    有生命值的Item类型
    """
    def __init__(self, *args, hp: Hpv, **kwargs):
        super(HpItem, self).__init__(*args, **kwargs)
        self.hp = hp

    def recover(self, num: int):
        """
        恢复生命值
        """
        self.hp.gain(num)

    def lose(self, num: int):
        """
        失去生命值
        """
        self.hp.lose(num)

    def cure(self):
        """
        补满生命值
        """
        self.hp.resume()

    def kill(self) -> None:
        """
        直接击杀
        """
        self.hp.lose(self.hp.left)

    def alive(self):
        """
        是否存活
        """
        return self.hp.left > 0

class SimpleItem(Item):
    """
    简单对象，只有一张图片
    """
    def __init__(self, *args, f: FrameSingle, **kwargs):
        super(SimpleItem, self).__init__(
            *args,
            media = Media({
                ORD: {
                    ACTIONS: [{
                        AUDIO: None,
                        FRAME: FrameGroup([f])
                    }],
                    ITER_TIME: 1
                }
            }, ORD),
            **kwargs
        )

    def update(self, *args, **kwargs) -> bool:
        """
        无需update
        """
        return True

class TransformableItem(Item):
    """
    使用pygame.transform相关的对象
    """
    def __init__(self, *args, **kwargs):
        super(TransformableItem, self).__init__(*args, **kwargs)
        self.__origin_image = self.media.image
        self.__image = self.__origin_image
        self.__transform_stack = []

    def rotate(self, angle: float):
        self.__transform_stack.append((pygame.transform.rotate, (angle, )))
        self.__image = pygame.transform.rotate(self.__image, angle)

    def rotozoom(self, angle: float, scale: float):
        self.__transform_stack.append((pygame.transform.rotozoom, (angle, scale)))
        self.__image = pygame.transform.rotozoom(self.__image, angle, scale)

    def scale2x(self):
        self.__transform_stack.append((pygame.transform.scale2x, ()))
        self.__image = pygame.transform.scale2x(self.__image)

    def smoothscale(self, size):
        self.__transform_stack.append((pygame.transform.smoothscale, (size, )))
        self.__image = pygame.transform.smoothscale(self.__image, size)

    def chop(self, rect):
        self.__transform_stack.append((pygame.transform.chop, (rect, )))
        self.__image = pygame.transform.chop(self.__image, rect)

    def flip(self, flp_x: bool = False, flp_y: bool = False):
        assert isinstance(flp_x, bool) and isinstance(flp_y, bool), 'Bool expected.'
        self.__transform_stack.append((pygame.transform.flip, (flp_x, flp_y)))
        self.__image = pygame.transform.flip(self.__image, flp_x, flp_y)

    def scale(self, size: tuple):
        self.__transform_stack.append((pygame.transform.scale, (size,)))
        self.__image = pygame.transform.scale(self.__image, size)

    def back_transformation(self):
        """
        此次应用不会马上生效！
        """
        self.__transform_stack.pop()

    def update(self, *args, **kwargs) -> bool:
        if self.media.image != self.__origin_image:
            self.__image = self.media.image
            for transform, a in self.__transform_stack:
                self.__image = transform(self.__image, *a)
            self.__origin_image = self.media.image
        return super(TransformableItem, self).update(*args, **kwargs)


    @property
    def image(self):
        return self.__image


__all__ = ['Item', 'MovableItem', 'StatefulItem', 'HpItem', 'Hpv', 'SimpleItem', 'TransformableItem']
