import pygame
from ..plane import *
from esign import *
from src.boundlrtb import Boundlftb
from src.bound import BoundLineSymmetry
from src.hp import *
from src.weapon import *
from .playerplane import *


class Player:
    """
    玩家类
    """
    def __init__(self, *args, plane: PlayerPlane, **kwargs):
        self.__plane = plane

    @property
    def plane(self) -> PlayerPlane:
        return self.__plane

    def draw(self, screen: pygame.Surface):
        self.plane.draw(screen)

    def w_key(self):
        pass
    def a_key(self):
        pass
    def s_key(self):
        pass
    def d_key(self):
        pass
    def wa_key(self):
        pass
    def wd_key(self):
        pass
    def sa_key(self):
        pass
    def sd_key(self):
        pass
    def space_key(self):
        pass

    def update(self, enemy_group):
        """
        通过键盘控制运动
        """
        self.plane.update(enemy_group)
        if self.plane.state == self.plane.PLAIN:
            keys = pygame.key.get_pressed()
            w = keys[pygame.K_w]
            a = keys[pygame.K_a]
            s = keys[pygame.K_s]
            d = keys[pygame.K_d]
            space = keys[pygame.K_SPACE]
            if w and not s:
                if a and not d:
                    self.wa_key()
                elif d and not a:
                    self.wd_key()
                else:
                    self.w_key()
                    self.plane.down(self.plane.down_hor)
            elif s and not w:
                if a and not d:
                    self.sa_key()
                elif d and not a:
                    self.sd_key()
                else:
                    self.s_key()
                    self.plane.down(self.plane.down_hor)
            else:
                if a and not d:
                    self.a_key()
                elif d and not a:
                    self.d_key()
                else:
                    self.plane.down(self.plane.down_hor)
                self.plane.down(self.plane.down_ver)
            if space:
                self.space_key()

class SinglePlayer(Player):
    """
    单人游戏玩家
    """
    def w_key(self):
        self.plane.acce(self.plane.TOP_ACCE)
    def a_key(self):
        self.plane.acce(self.plane.LEFT_ACCE)
    def s_key(self):
        self.plane.acce(self.plane.BOTTOM_ACCE)
    def d_key(self):
        self.plane.acce(self.plane.RIGHT_ACCE)
    def wa_key(self):
        self.plane.acce(self.plane.LEFT_TOP_ACCE)
    def wd_key(self):
        self.plane.acce(self.plane.RIGHT_TOP_ACCE)
    def sa_key(self):
        self.plane.acce(self.plane.LEFT_BOTTOM_ACCE)
    def sd_key(self):
        self.plane.acce(self.plane.RIGHT_BOTTOM_ACCE)
    def space_key(self):
        self.plane.fire()

@stateDefine(
    'INVINCIBLE',   # 玩家刚加入处于无敌状态
    'PLAIN'         # 出于正常状态
)
class OnlinePlayer(Player):
    """
    线上玩家
    """
    def __init__(self, *args, id, **kwargs):
        super(OnlinePlayer, self).__init__(*args, **kwargs)
        self.__id = id
        self.instructors = []
        self.switch('INVINCIBLE')

    @property
    def id(self):
        return self.__id

    def w_key(self):
        self.instructors.append({
            'type': 'player_instructor',
            'value': {
                'id': self.id,
                'direction': 'w'
            }
        })
    def a_key(self):
        self.instructors.append({
            'type': 'player_instructor',
            'value': {
                'id': self.id,
                'direction': 'a'
            }
        })
    def s_key(self):
        self.instructors.append({
            'type': 'player_instructor',
            'value': {
                'id': self.id,
                'direction': 's'
            }
        })
    def d_key(self):
        self.instructors.append({
            'type': 'player_instructor',
            'value': {
                'id': self.id,
                'direction': 'd'
            }
        })
    def wa_key(self):
        self.instructors.append({
            'type': 'player_instructor',
            'value': {
                'id': self.id,
                'direction': 'wa'
            }
        })
    def wd_key(self):
        self.instructors.append({
            'type': 'player_instructor',
            'value': {
                'id': self.id,
                'direction': 'wd'
            }
        })
    def sa_key(self):
        self.instructors.append({
            'type': 'player_instructor',
            'value': {
                'id': self.id,
                'direction': 'sa'
            }
        })
    def sd_key(self):
        self.instructors.append({
            'type': 'player_instructor',
            'value': {
                'id': self.id,
                'direction': 'sd'
            }
        })
    def space_key(self):
        self.instructors.append({
            'type': 'player_instructor',
            'value': {
                'id': self.id,
                'direction': 'space'
            }
        })

    def process(self, info: dict):
        ins = info['direction']
        if ins == 'w':
            self.plane.acce(self.plane.TOP_ACCE)
        elif ins == 'a':
            self.plane.acce(self.plane.LEFT_ACCE)
        elif ins == 's':
            self.plane.acce(self.plane.BOTTOM_ACCE)
        elif ins == 'd':
            self.plane.acce(self.plane.RIGHT_ACCE)
        elif ins == 'wa':
            self.plane.acce(self.plane.LEFT_TOP_ACCE)
        elif ins == 'wd':
            self.plane.acce(self.plane.RIGHT_TOP_ACCE)
        elif ins == 'sa':
            self.plane.acce(self.plane.LEFT_BOTTOM_ACCE)
        elif ins == 'sd':
            self.plane.acce(self.plane.RIGHT_BOTTOM_ACCE)
        elif ins == 'space':
            self.plane.fire()

    def update(self, enemy_group):
        super(OnlinePlayer, self).update(enemy_group)
        if self.state == self.INVINCIBLE:
            self.plane.cure()


__all__ = ['Player', 'SinglePlayer', 'OnlinePlayer']