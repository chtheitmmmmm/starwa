from . import *
from esign import *
from mediapool import *

_shoot_audio    = ap.bail('bullet', 'shoot')   # list
_boom_audio     = ap.bail('bullet', 'boom')     # list
_bullet_water   = fp.bail('plane', 'bullet', 'player')    # dict

_speed           = Vector2(0, -5)
_acce            = Vector2(0, -1)
_hurt_red_bar    = 10      # 两翼子弹伤害
_hurt_red_point  = 15    # 中间子弹伤害
_hurt_blue_bar   = 9
_hurt_blue_point = 12

_red_bar = Bullet(
    media       = Media({
        ORD: {
            ACTIONS: [{
                AUDIO: _shoot_audio[0],
                FRAME: FrameGroup(_bullet_water['red']['bar'])
            }],
            ITER_TIME: 1
        },
        'boom': {
            ACTIONS: [{
                AUDIO: _boom_audio[0],
                FRAME: FrameGroup(_bullet_water['red']['effect'])
            }],
            ITER_TIME: 1
        }
    }, ORD),
    pos         = Vector2(0, 0),
    speed       = _speed,
    accelerate  = _acce,
    hurt        = _hurt_red_bar
)

_red_point = Bullet(
    media       = Media({
        ORD: {
            ACTIONS: [{
                AUDIO: _shoot_audio[0],
                FRAME: FrameGroup(_bullet_water['red']['point'])
            }],
            ITER_TIME: 1
        },
        'boom': {
            ACTIONS: [{
                AUDIO: _boom_audio[0],
                FRAME: FrameGroup(_bullet_water['red']['effect'])
            }],
            ITER_TIME: 1
        }
    }, ORD),
    pos         = Vector2(0, 0),
    speed       = _speed,
    accelerate  = _acce,
    hurt        = _hurt_red_point
)

_blue_bar = Bullet(
    media       = Media({
        ORD: {
            ACTIONS: [{
                AUDIO: _shoot_audio[0],
                FRAME: FrameGroup(_bullet_water['blue']['bar'])
            }],
            ITER_TIME: 1
        },
        'boom': {
            ACTIONS: [{
                AUDIO: _boom_audio[0],
                FRAME: FrameGroup(_bullet_water['blue']['effect'])
            }],
            ITER_TIME: 1
        }
    }, ORD),
    pos         = Vector2(0, 0),
    speed       = _speed,
    accelerate  = _acce,
    hurt        = _hurt_blue_bar
)

_blue_point = Bullet(
    media       = Media({
        ORD: {
            ACTIONS: [{
                AUDIO: _shoot_audio[0],
                FRAME: FrameGroup(_bullet_water['blue']['point'])
            }],
            ITER_TIME: 1
        },
        'boom': {
            ACTIONS: [{
                AUDIO: _boom_audio[0],
                FRAME: FrameGroup(_bullet_water['blue']['effect'])
            }],
            ITER_TIME: 1
        }
    }, ORD),
    pos         = Vector2(0, 0),
    speed       = _speed,
    accelerate  = _acce,
    hurt        = _hurt_blue_point
)

@firenumfy(1)
class PlayerGun(ConstantBulletGun):
    pass

lion_weapon = WeaponGroup([
    (PlayerGun(_red_bar), Vector2(1 / 5, 20)),
    (PlayerGun(_red_point), Vector2(1 / 2, 0)),
    (PlayerGun(_red_bar), Vector2(4 / 5, 20))
])

bird_weapon = WeaponGroup([
    (PlayerGun(_blue_bar), Vector2(1 / 6, 10)),
    (PlayerGun(_blue_point), Vector2(1 / 3, 3)),
    (PlayerGun(_blue_point), Vector2(2 / 3, 3)),
    (PlayerGun(_blue_bar), Vector2(5 / 6, 10))
])

__all__ = [
    'lion_weapon',
    'bird_weapon'
]