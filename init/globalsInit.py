import random

import pygame
from . import graphicsInit, audioInit, constants, grandfatherInit
from myGametools import mypoint, mySprite
from classes.buttons import button, button_group
from functions import selfAdapt, medalign
from classes import background, bound, boundlrtb
from classes.planes.parture import hp
from classes.planes.player import players, playerplane
from classes.planes.enemys import sa_1, enemygroup
from classes.planes.parture import controlcenter, engine
from classes.planes.parture.weapon import gun, bullet

graphics = graphicsInit.alls
# 起始界面
menu = background.BackGround(graphics['begin ui'], mypoint.Mypoint((0, 0)))
# 标题
logo = mySprite.MySprite(graphics['title'], mypoint.Mypoint((0,0)))
# 加载存档按钮
read_grandfather = button.Button(graphics['read grandfather button'], audioInit.read_grandfather_audio, mypoint.Mypoint((0,0)))
medalign.midalign(menu, read_grandfather, 1)
grandfather_bg = background.BackGround(graphics['grandfather bg'], mypoint.Mypoint((0,0)))
confirm_grand = button.Button(graphics['confirm grandfather'], audioInit.confirm_grandfather, mypoint.Mypoint((100, 650)), None, None, True)
cancel_grand = button.Button(graphics['cancel grandfather'], audioInit.cancel_grandfather, mypoint.Mypoint((430, 650)))
confirm_cancel_grand = button_group.con_can_grand(confirm_grand, cancel_grand)

# 开始按钮
bebu = button.Button(graphics['begin button'], audioInit.read_grandfather_audio, mypoint.Mypoint((0,0)))
medalign.midalign(menu, bebu, 1)
menu_buttons = button_group.Menu_Buttons(bebu)


# 存档活动页面
leftbound = 90
topbound = 200
bottombound = 680
#
# grands = grandfatherInit.Grandfathers(
#     boundlrtb.Boundlftb(
#         bound.BoundUnit(
#             leftbound,
#             leftbound+constants.GRAND_SIZE[0]
#         ),
#         bound.BoundUnit(
#             topbound,
#             bottombound
#         )))

# 界面bound
screen_bound = boundlrtb.Boundlftb(
            bound.BoundUnit(0, constants.SCREEN_SIZE[0]),
            bound.BoundUnit(0, constants.SCREEN_SIZE[1])
        )

# 玩家飞船
lionspeedbound = boundlrtb.Boundlftb(bound.BoundUnit(-10, 10), bound.BoundUnit(-10, 4))
lionengine = engine.Engine(lionspeedbound)
lioncontrolcenter = controlcenter.ControlCenter(lionengine)
lionhp = hp.HpFrameBar(
    hp.HpBarSprite(hp.Hp(constants.LionHp), graphics['playerhpbar'], mypoint.Mypoint(
        (constants.LocHp[0] - graphics['playerhpbar'].image.get_width() // 2,
         constants.LocHp[1] - graphics['playerhpbar'].image.get_height() // 2
         ))),
    mySprite.MyMoveSprite(graphics['playerhpframe'], mypoint.Mypoint(
        (constants.LocHp[0] - graphics['playerhpframe'].image.get_width() // 2,
         constants.LocHp[1] - graphics['playerhpframe'].image.get_height() // 2)
    ))
)
lionweaponbullet = bullet.Bullet(
    10,
    graphics['player bullet red'],
    audioInit.lionbullet_audio,
    mypoint.Mypoint((0,0)),
    constants.LionBulletSpeed,
    constants.LionBulletAcce
)
lionweapon = gun.Gun(
    constants.LionBulletInterval,
    lionweaponbullet
)
lionplane = playerplane.PlayerPlane(
    'LION',
    graphics['player plane lion'],
    mypoint.Mypoint((0,0)),
    audioInit.lion_audio,
    lioncontrolcenter,
    lionweapon,
    lionhp,
    *constants.LionGunInterval
)

PLAYERS = players.Players(lionplane)

# 敌人飞船
sa_1engine = engine.Sa_1_Engine()
sa_1controlcneter = controlcenter.Sa_1_Controlcenter(sa_1engine)
sa_1weaponbullet = bullet.Bullet(
    3,
    graphics['sa_1 bullet'],
    audioInit.lionbullet_audio,
    mypoint.Mypoint((0,0)),
    constants.sa_1BulletSpeed,
    constants.sa_1BulletAcce
)
sa_1gun = gun.Sa_1_Gun(
    constants.sa_1BulletInterval,
    sa_1weaponbullet
)
sa1hpframebar = hp.Enemy_HpFrameBar(
    hp.HpBarSprite(hp.Hp(constants.sa_1Hp),
                   graphics['sa_1 hpbar'],
                   mypoint.Mypoint((100, 100))
                   ),
    mySprite.MyMoveSprite(graphics['sa_1 hpframe'],
                          mypoint.Mypoint((100, 100))
                          ),
)
Sa_1 = sa_1.Sa_1(
    'Sa_1',
    graphics['sa_1'],
    mypoint.Mypoint((100, 300)),
    audioInit.sa_1_audio,
    sa_1controlcneter,
    sa_1gun,
    sa1hpframebar,
    *constants.sa_1GunInterval,
)
Enemygroup = enemygroup.EnemyGroup(Sa_1, internal=2300)



GAMEBGING = 0
GAMEOVER  = 1
READYGO   = 2
READ_GRAND = 3
flags = [False, False, False, False]

battlemap1 = background.VerticalUSBG(graphics['battle map1'], mypoint.Mypoint((0,0)), speed=1)

def convert_screen_init(screen:pygame.Surface):
    selfAdapt.selfadapttop(battlemap1, screen)
    medalign.midalign_vertical(battlemap1, lionplane.controlcenter, medalign.STICKS1)










