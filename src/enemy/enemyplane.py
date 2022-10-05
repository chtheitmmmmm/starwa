import copy
from src.plane import *
from mediapool import *
from src.hp import *
from src.weapon import *
from esign import *
from src.boundlrtb import Boundlftb
from src.bound import *
from src.constants import constants

_window_size = constants['meta']['windowSize']

class EnemyPlane(ArmedPlane):
    """
    敌人类
    {
        'ord'  : ...
        'boom' : ...
    }
    """
    _selfbound = Boundlftb(BoundUnit(0, _window_size[0]), BoundUnit(0, _window_size[1] * 2/3))
    _speedbound = Boundlftb(BoundUnit(-7, 7), BoundUnit(-4, 4))
    __weapon_speed = Vector2(0, 3)
    hpbar = HpBar(  # 敌人血条
        SimpleItem(f=fp.bail('plane', 'hp', 'bar', 'enemy')[0], pos=Vector2(0, 0)).media,
        SimpleItem(f=fp.bail('plane', 'hp', FRAME, 'enemy')[0], pos=Vector2(0, 0)).media
    )
    _plane_boom = {
        ACTIONS: [{
            AUDIO: ap.bail('plane', 'boom', 'enemy')[0],
            FRAME: FrameGroup(fp.bail('plane', 'boom', 'enemy'))
        }],
        ITER_TIME: 1
    }
    weapontypes = {}
    def __init_subclass__(
            cls,
            code,
            fpindex,
            hp          = 100,
            activearea  = _selfbound,
            relas       = [(Vector2(1 / 2, 0), 1)],
            bullet      = Bullet(
                media   = Media({
                    ORD: {
                        ACTIONS:[{
                            AUDIO: None,
                            FRAME: FrameGroup([fp.bail('plane', 'bullet', 'enemy', 'red')[0]]),
                        }] ,
                        ITER_TIME: 1
                    },
                    'boom': {
                        ACTIONS: [{
                            AUDIO: ap.bail('bullet', 'boom')[0],
                            FRAME: FrameGroup(fp.bail('plane', 'bullet', 'enemy', 'red')[1:]),
                        }],
                        ITER_TIME: 1
                    }
                }, ORD),
                pos     = Vector2(0, 0),
                speed   = __weapon_speed,
                accelerate = Vector2(0, 0.2),
                hurt    = 3),
            ):
        """
        :param fpindex: 外观在fp中的下标号
        :param hp: 总生命值
        :param weaponoutput: 武器输出，默认为伤害为3的sa1子弹
        :param relas: 内容为二元组的列表，元组第一个元素为相对位置，第二个元素为连发炮弹数目
        """
        assert cls._selfbound & activearea, 'Conflict area against bound!'
        cls.code = code
        cls.activearea = activearea
        cls.bullet = bullet # 子弹
        firenums = set(num for rela, num in relas)
        for n in firenums:  # 生成所有不存在的枪支类型
            if not EnemyPlane.weapontypes.get(n):
                @firenumfy(n)
                class gun(ConstantBulletGun):
                    pass
                EnemyPlane.weapontypes[n] = gun
        weapongroup = WeaponGroup([(EnemyPlane.weapontypes[relas[i][1]](bullet), relas[i][0]) for i in range(len(relas))])   # 武器群对象
        def __init__(self, pos: Vector2):
            super(EnemyPlane, self).__init__(
                media       = Media({
                    ORD: {
                        ACTIONS: [{
                            FRAME: FrameGroup([fp.bail('plane', 'apperance', 'enemy')[fpindex]]),
                            AUDIO: None
                        }],
                        ITER_TIME: 1
                    },
                    'boom': copy.deepcopy(EnemyPlane._plane_boom)
                }, ORD),
                pos         = pos,
                acce        = (0.2, ) * 4,
                hp          = Hpv(hp, hp),
                hpbar       = EnemyPlane.hpbar.copy(),
            )
            selfweapongroup = weapongroup.copy()
            self.configureWeapon(selfweapongroup)
        cls.__init__ = __init__
    def update(self, enemy_group):
        super().update(enemy_group)



class Sa_1Plane(
    EnemyPlane,
    code        = 1,
    fpindex     = 0,
    activearea  = Boundlftb.From(   # sa1战机倾向于分布在战场中部
        Vector2(_window_size[0] * 1/5, _window_size[0] * 4/5),
        Vector2(_window_size[1] * 1 / 3, _window_size[1] * 2 / 3)
    )
):
    """
    Sa_1敌机
    生命值：100
    武器：一次在最中间发射一枚子弹
    """

class Sc_1Plane(
    EnemyPlane,
    code        = 2,
    fpindex     = 1,
    hp          = 120,
    activearea  = Boundlftb.From(   # sc1战机倾向于分布在战场中部左侧
        Vector2(_window_size[0] * 1/3, _window_size[0] * 2/3),
        Vector2(_window_size[1] * 1 / 3, _window_size[1] * 2 / 3)
    )
):
    """
    Sc_1战机
    生命值：120
    武器：一次在最中间发射两枚子弹
    """

class Sc_2Plane(
    EnemyPlane,
    code        = 3,
    fpindex     = 2,
    hp          = 150,
    activearea  = Boundlftb.From(   # sc2战机倾向于分布在战场中部右侧
        Vector2(_window_size[0] * 2 / 3, _window_size[0]),
        Vector2(_window_size[1] * 1 / 3, _window_size[1] * 2 / 3)
    )
):
    """
    Sc_2战机
    生命值：150
    武器：一次在最中间发射三枚子弹
    """

class Sc_3Plane(
    EnemyPlane,
    code        = 4,
    fpindex     = 3,
    hp          = 200,
    activearea  = Boundlftb.From(   # sc3 倾向于分布在战场左上方
        Vector2(_window_size[0] * 1/3, _window_size[0] * 2 / 3),
        Vector2(0, _window_size[1] * 1 / 3)
    ),
    relas       = [
        (Vector2(1/4, 0), 2),
        (Vector2(3/4, 0), 2)
    ]
):
    """
    Sc_3 战机
    生命值：200
    武器：一次在两侧分别发射两枚子弹
    """

class Sc_4Plane(
    EnemyPlane,
    code        = 5,
    fpindex     = 4,
    hp          = 80,
    activearea  = Boundlftb.From(   # sc4 倾向于分布在战场后方
      Vector2(0, _window_size[0]),
      Vector2(0, _window_size[1] * 1 / 3)
    ),
    relas       = [
        (Vector2(1/5, 0), 2),
        (Vector2(1/2, 20), 3),
        (Vector2(4/5, 0), 2)
    ]
):
    """
    Sc_4 战机
    生命值：60
    武器：一次在身体正中发射三枚子弹，在两侧各发射两枚子弹
    """


enemyplanetypes = [Sc_1Plane]

__all__ = [
    'EnemyPlane',
    'enemyplanetypes',
    'Sa_1Plane' ,
    'Sc_1Plane' ,
    'Sc_2Plane' ,
    'Sc_3Plane' ,
    'Sc_4Plane' ,
]