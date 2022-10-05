from esign import *
from ..plane import *
from mediapool import *
from src.bound import *
from src.hp import *
from src.weapon.playerweapon import *
from src.constants import constants

class PlayerPlane(ArmedPlane):
    """
    可控制运动的飞机，限制自身运动范围，并管理武器弹药的创建删除等
    media: {
        'ord': ...
        'l1': ...
        'l2': ...
        'l3': ...
        'r1': ...
        'r2': ...
        'r3': ...
    }
    """
    acce_pull = 1.5
    acce_def = 4
    down_hor = 10
    down_ver = 20
    speedstep = BoundLineSymmetry([6, 8, 12])  # 玩家飞机的姿态界限
    hpbar = HpBar(
        Media({
        ORD: {
            ACTIONS: [{
                AUDIO: None,
                FRAME: FrameGroup(fp.bail('plane', 'hp', 'bar', 'player'))
            }]
        }
    }, ORD),
        Media({
        ORD: {
            ACTIONS: [{
                AUDIO: None,
                FRAME: FrameGroup(fp.bail('plane', 'hp', FRAME, 'player'))
            }]
        }
    }, ORD)
    )

    def __init__(self, *args, hprelative: bool=False, hppos: Vector2=Vector2(0, 0), **kwargs):
        super(PlayerPlane, self).__init__(*args, **kwargs)
        self.apperancestate = StateMachine('L3', 'L2', 'L1', 'ORD', 'R1', 'R2', 'R3')
        self.apperancestate.switch('ORD')
        if not hprelative:
            self.hpbar.configure(hppos, self, hprelative)
        else:
            # 希望在垂直方向对其
            centerx = (self.rect.w - self.hpbar.hpf.rect.w) / 2
            self.hpbar.configure(Vector2(centerx, hppos.y), self, hprelative)

    def step(self):
        step = self.speedstep.detect_section(self.speed.x)
        if step == 0:
            if self.apperancestate.value != 'L3':
                self.left3()
        elif step == 1:
            if self.apperancestate.value != 'L2':
                self.left2()
        elif step == 2:
            if self.apperancestate.value != 'L1':
                self.left1()
        elif step == 3:
            if self.apperancestate.value != 'ORD':
                self.ord()
        elif step == 4:
            if self.apperancestate.value != 'R1':
                self.right1()
        elif step == 5:
            if self.apperancestate.value != 'R2':
                self.right2()
        elif step == 6:
            if self.apperancestate.value != 'R3':
                self.right3()

    def left3(self):
        self.apperancestate.switch('L3')
        self.action('l3')

    def left2(self):
        self.apperancestate.switch('L2')
        self.action('l2')

    def left1(self):
        self.apperancestate.switch('L1')
        self.action('l1')

    def ord(self):
        self.apperancestate.switch('ORD')
        self.action('ord')

    def right3(self):
        self.apperancestate.switch('R3')
        self.action('r3')

    def right2(self):
        self.apperancestate.switch('R2')
        self.action('r2')

    def right1(self):
        self.apperancestate.switch('R1')
        self.action('r1')

    def down(self, direction = down_hor):
        if direction == self.down_ver:
            if self.accelerate[1]:
                self.accelerate[1] = 0
            if self.speed[1] > 0:
                self.speed[1] -= self.acce_def
                if self.speed[1] < 0:
                    self.speed[1] = 0
            elif self.speed[1] < 0:
                self.speed[1] += self.acce_def
                if self.speed[1] > 0:
                    self.speed[1] = 0
        elif direction == self.down_hor:
            if self.accelerate[0]:
                self.accelerate[0] = 0
            if self.speed[0] > 0:
                self.speed[0] -= self.acce_def
                if self.speed[0] < 0:
                    self.speed[0] = 0
            elif self.speed[0] < 0:
                self.speed[0] += self.acce_def
                if self.speed[0] > 0:
                    self.speed[0] = 0

    def update(self, aim_group: AbstractGroup | None):
        super(PlayerPlane, self).update(aim_group)
        self.step()

    def __init_subclass__(
            cls, *,
            code,   # 飞机代号
            media,  # 飞机媒体
            acce,   # 飞机加速度，四元组
            hp,     # 飞机生命值
            weapon, # 飞机武器
    ):
        cls.code = code
        def __init__(self, *args, hprelative: bool=False, hppos: Vector2=Vector2(0, 0), **kwargs):
            """
            仅需传入 hprelative 和 hppos 即可
            """
            super(type(self), self).__init__(
                media = media.copy(),
                pos = Vector2(0, constants["locations"]["planeInitialVertical"]),
                acce = acce,
                hp = hp,
                hpbar = cls.hpbar.copy(),
                hprelative = hprelative,
                hppos = hppos
            )
            self.configureWeapon(weapon.copy())
        cls.__init__ = __init__

class LionPlane(
    PlayerPlane,
    code = 1,
    media = Media({
                'l1': {
                    ACTIONS: [{
                        AUDIO: None,
                        FRAME: FrameGroup([fp.bail('plane', 'apperance', 'player', 'lion', 'plane')[0]])
                    }],
                    ITER_TIME: 1
                },
                'l2': {
                    ACTIONS: [{
                        AUDIO: None,
                        FRAME: FrameGroup([fp.bail('plane', 'apperance', 'player', 'lion', 'plane')[1]])
                    }],
                    ITER_TIME: 1
                },
                'l3': {
                    ACTIONS: [{
                        AUDIO: None,
                        FRAME: FrameGroup([fp.bail('plane', 'apperance', 'player', 'lion', 'plane')[2]])
                    }],
                    ITER_TIME: 1
                },
                ORD: {
                    ACTIONS: [{
                        AUDIO: None,
                        FRAME: FrameGroup([fp.bail('plane', 'apperance', 'player', 'lion', 'plane')[3]])
                    }],
                    ITER_TIME: 1
                },
                'r1': {
                    ACTIONS: [{
                        AUDIO: None,
                        FRAME: FrameGroup([fp.bail('plane', 'apperance', 'player', 'lion', 'plane')[4]])
                    }],
                    ITER_TIME: 1
                },
                'r2': {
                    ACTIONS: [{
                        AUDIO: None,
                        FRAME: FrameGroup([fp.bail('plane', 'apperance', 'player', 'lion', 'plane')[5]])
                    }],
                    ITER_TIME: 1
                },
                'r3': {
                    ACTIONS: [{
                        AUDIO: None,
                        FRAME: FrameGroup([fp.bail('plane', 'apperance', 'player', 'lion', 'plane')[6]])
                    }],
                    ITER_TIME: 1
                },
                'boom': {
                    ACTIONS: [{
                        AUDIO: ap.bail('plane', 'boom', 'player')[0],
                        FRAME: FrameGroup(fp.bail('plane', 'boom', 'player'))
                    }],
                    ITER_TIME: 1
                }
            }, ORD),
    acce  = (1, 0.5, 1.5, 1.5),
    hp = Hpv(120),
    weapon = lion_weapon
):
    pass

class BirdPlane(
    PlayerPlane,
    code = 2,
    media = Media({
                    'l1': {
                        ACTIONS: [{
                            AUDIO: None,
                            FRAME: FrameGroup([fp.bail('plane', 'apperance', 'player', 'bird', 'plane')[0]])
                        }],
                        ITER_TIME: 1
                    },
                    'l2': {
                        ACTIONS: [{
                            AUDIO: None,
                            FRAME: FrameGroup([fp.bail('plane', 'apperance', 'player', 'bird', 'plane')[1]])
                        }],
                        ITER_TIME: 1
                    },
                    'l3': {
                        ACTIONS: [{
                            AUDIO: None,
                            FRAME: FrameGroup([fp.bail('plane', 'apperance', 'player', 'bird', 'plane')[2]])
                        }],
                        ITER_TIME: 1
                    },
                    ORD: {
                        ACTIONS: [{
                            AUDIO: None,
                            FRAME: FrameGroup([fp.bail('plane', 'apperance', 'player', 'bird', 'plane')[3]])
                        }],
                        ITER_TIME: 1
                    },
                    'r1': {
                        ACTIONS: [{
                            AUDIO: None,
                            FRAME: FrameGroup([fp.bail('plane', 'apperance', 'player', 'bird', 'plane')[4]])
                        }],
                        ITER_TIME: 1
                    },
                    'r2': {
                        ACTIONS: [{
                            AUDIO: None,
                            FRAME: FrameGroup([fp.bail('plane', 'apperance', 'player', 'bird', 'plane')[5]])
                        }],
                        ITER_TIME: 1
                    },
                    'r3': {
                        ACTIONS: [{
                        AUDIO: None,
                        FRAME: FrameGroup([fp.bail('plane', 'apperance', 'player', 'bird', 'plane')[6]])
                    }],
                        ITER_TIME: 1
                    },
                    'boom': {
                        ACTIONS: [{
                            AUDIO: ap.bail('plane', 'boom', 'player')[0],
                            FRAME: FrameGroup(fp.bail('plane', 'boom', 'player'))
                        }],
                        ITER_TIME: 1
                    }
            }, ORD),
    acce = (1, 0.5, 1.5, 1.5),
    hp = Hpv(100),
    weapon = bird_weapon,
):
    pass

playerplanetypes = [LionPlane, BirdPlane]

__all__ = ['PlayerPlane', 'LionPlane', 'BirdPlane', 'playerplanetypes']