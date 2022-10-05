import json

import pygame, time, random
from esign import *
from .enemyplane import *
from src.constants import constants
from ..plane import *
from src.msg import Msg
from .enemy import Enemy

_fps = 1 / constants['meta']['FPS']
_encoding = constants['meta']['net']['encoding']

class EnemyGroup(pygame.sprite.Group):
    """
    敌机的产生、运动、射击逻辑均交由此类管理。
    这些动作又分为主动和被动：
        主动即为本机自主运算结果
        被动即为从事件中获取运算结果
    """
    def draw(self, screen: pygame.Surface):
        for e in self.sprites():
            e.draw(screen)

    def __init__(self, *planetypes: EnemyPlane):
        super().__init__()
        self.planetypes = planetypes  # 所有飞机种类

    def generate(self):
        tp  = random.choice(self.planetypes)
        pos = tp.activearea.randompoint()
        return tp(pos)

    def randomMove(self, plane: EnemyPlane) -> int:
        """
        随机运动计算，根据战机的 activearea
        算法：
            敌机每若干帧执行一次加速
            在 activearea 的水平方向和垂直方向，在中心线的两侧，离中心线越远，越有可能向中心线加速
            若超出 activearea 范围，则一定向中心线加速。
            特点：怪物在中心线那分布较均匀，怪物不会离开 activearea 太远
        返回怪物的运动方向，若没有运动则返回空字符串
        """
        if random.random() < 1 / 10:
            if plane.rect.centerx >= plane.activearea.xmedium:
                if random.random() < (plane.rect.centerx - plane.activearea.xmedium) / plane.activearea.xlength:
                    return 'a'
                else:
                    return 'd'
            else:
                if random.random() < (plane.activearea.xmedium - plane.rect.centerx) / plane.activearea.xlength:
                    return 'd'
                else:
                    return 'a'
            if plane.rect.centery >= plane.activearea.ymedium:
                if random.random() < (plane.rect.centery - plane.activearea.ymedium) / plane.activearea.ylength:
                    return 'w'
                else:
                    return 's'
            else:
                if random.random() < (plane.activearea.ymedium - plane.rect.centery) / plane.activearea.ylength:
                    return 's'
                else:
                    return 'w'
        return ''

    def randomShoot(self, plane: EnemyPlane) -> bool:
        """
        随机射击计算
        算法：
            每个怪物平均每180帧发动一次希冀
        返回是否射击
        """
        if random.random() < _fps / 3:
            return True
        return False

    def randomGenerate(self) -> EnemyPlane:
        """
        随机产生计算
        算法：
            平均每 3 * FPS 帧产生一个敌人
        """
        if random.random() < 10 * _fps / (len(self.sprites()) + 1):
            plane = self.generate()
            return plane
        return None

    def update(self, enemy_group):
        for enemy in self.sprites():
            if enemy.state == enemy.DELETABLE:
                self.remove(enemy)
            else:
                enemy.update(enemy_group)

class OfflineEnemyGroup(EnemyGroup):
    """
    自主执行怪物移动、产生、发射
    """
    def update(self, enemy_group):
        for p in self.sprites():
            p.update(enemy_group)
            if p.state != p.BOOMING and p.state != p.BOOMED and p.state != p.DELETABLE:
                direction = self.randomMove(p)
                if direction == 'w':
                    p.acce(p.TOP_ACCE)
                elif direction == 'a':
                    p.acce(p.LEFT_ACCE)
                elif direction == 's':
                    p.acce(p.BOTTOM_ACCE)
                elif direction == 'd':
                    p.acce(p.RIGHT_ACCE)
                if self.randomShoot(p):
                    p.fire()
            elif p.state == p.DELETABLE:
                self.remove(p)
        newplane = self.randomGenerate()
        if newplane:
            self.add(newplane)

@stateDefine('HOST', 'GUEST')
class OnlineEnemyGroup(EnemyGroup):
    """
    线上游戏敌群
    实现统一的 process 方法，通过状态定义是否为房主
    初始状态为 GUEST
    """
    def __init__(self, *args, **kwargs):
        super(OnlineEnemyGroup, self).__init__(*args, **kwargs)
        self.enemys = []    # 维护一个 enemy 列表
        self.switch('GUEST')

    def getPlaneById(self, id: float):
        for enemy in self.enemys:
            if enemy.id == id:
                return enemy.plane
        return None

    def getEnemyType(self, code: int):
        for enemytype in enemyplanetypes:
            if enemytype.code == code:
                return enemytype
        return None

    def init(self, globalmsg: dict):
        """
        根据  globalmsg 来初始化怪物群
        将 global 消息的 value字段传入即可
        """
        for enemyinfo in globalmsg['enemys']:
            newenemytype = self.getEnemyType(enemyinfo['code'])
            newenemy = Enemy(
                id = enemyinfo['id'],
                enemytype = newenemytype,
                pos = enemyinfo['pos']
            )
            self.enemys.append(newenemy)
            self.add(newenemy.plane)

    def process(self, info: dict):
        """
        处理从服务器返回的信息
        info 为 type为 enemy_instructor的Msg 的value
        """
        if info['instructor'] == 'add':
            newenemy = Enemy(
                id = info['id'],
                enemytype=self.getEnemyType(info['code']),
                pos = Vector2(*info['pos'])
            )
            self.enemys.append(newenemy)
            self.add(newenemy.plane)
        elif info['instructor'] == 'accelerate':
            plane = self.getPlaneById(info['id'])
            if plane:
                direction = info['direction']
                if direction == 'w':
                    plane.acce(plane.TOP_ACCE)
                elif direction == 'a':
                    plane.acce(plane.LEFT_ACCE)
                elif direction == 's':
                    plane.acce(plane.BOTTOM_ACCE)
                elif direction == 'd':
                    plane.acce(plane.RIGHT_ACCE)
                elif direction == 'wa':
                    plane.acce(plane.LEFT_TOP_ACCE)
                elif direction == 'wd':
                    plane.acce(plane.RIGHT_TOP_ACCE)
                elif direction == 'sa':
                    plane.acce(plane.LEFT_BOTTOM_ACCE)
                elif direction == 'sd':
                    plane.acce(plane.RIGHT_BOTTOM_ACCE)
                else:
                    raise ValueError('Unknown accelerate direction!')
            else:
                raise ValueError('No such plane!')
        elif info['instructor'] == 'shoot':
            plane = self.getPlaneById(info['id'])
            if plane:
                plane.fire()
            else:
                raise ValueError('No such plane!')
        else:
            raise ValueError('No such instructor!')

    def __host_update(self, enemy_group) -> list[dict]:
        """
        返回指令
        """
        super(OnlineEnemyGroup, self).update(enemy_group)
        instructors = []
        for enemy in self.enemys:
            if enemy.plane.state != enemy.plane.BOOMING and enemy.plane.state != enemy.plane.BOOMED and enemy.plane.state != enemy.plane.DELETABLE:
                direction = self.randomMove(enemy.plane)
                if direction:
                    instructors.append({
                        'type': 'enemy_instructor',
                        'value': {
                            'instructor': 'accelerate',
                            'id': enemy.id,
                            'direction': direction
                        }
                    })
                if self.randomShoot(enemy.plane):
                    instructors.append({
                        'type': 'enemy_instructor',
                        'value': {
                            'instructor': 'shoot',
                            'id': enemy.id,
                        }
                    })
            elif enemy.plane.state == enemy.plane.DELETABLE:
                self.remove(enemy.plane)
                self.enemys.remove(enemy)
        newplane = self.randomGenerate()
        if newplane:
            instructors.append({
                'type': 'enemy_instructor',
                'value': {
                    'instructor': 'add',
                    'id': time.time(),
                    'code': newplane.code,
                    'pos': [*newplane.pos]
                }
            })
        return instructors

    def update(self, enemy_group):
        if self.state == self.HOST:
            return self.__host_update(enemy_group)
        elif self.state == self.GUEST:
            super(OnlineEnemyGroup, self).update(enemy_group)
            return None

enemytypes = (Sa_1Plane, Sc_1Plane, Sc_2Plane, Sc_3Plane, Sc_4Plane)


__all__ = [
    'EnemyGroup',
    'OfflineEnemyGroup',
    'OnlineEnemyGroup',
]