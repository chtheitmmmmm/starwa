import pygame
from classes.media.frame import frame

alls = {
    'title': frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/game/bg/title/title.png').convert_alpha(), 1)],
    ]),

    'begin ui': frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/1.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/2.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/3.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/4.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/5.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/6.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/7.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/8.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/9.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/10.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/11.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/12.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/13.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/14.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/15.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/16.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/17.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/18.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/19.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/20.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/21.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/22.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/23.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/24.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/25.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/26.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/27.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/28.jpg').convert(), 10),
         frame.FrameNum(pygame.image.load('media/graphics/game/bg/readybg/29.jpg').convert(), 10)]
    ]),

    'begin button': frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/button/beginBotton/0.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/button/beginBotton/on.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/button/beginBotton/c.png').convert_alpha(), 20),
        frame.FrameNum(pygame.image.load('media/graphics/game/ui/button/beginBotton/on.png').convert_alpha(), 20)],
    ]),

    'read grandfather button': frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/button/read_grandfather/0.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/button/read_grandfather/on.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/button/read_grandfather/c.png').convert_alpha(), 1)]
    ]),

    'confirm grandfather': frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/button/grandfathercc/confirm/0.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/button/grandfathercc/confirm/on.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/button/grandfathercc/confirm/c.png').convert_alpha(), 20)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/button/grandfathercc/confirm/d.png').convert_alpha(), 1)]
    ], leisureframe=3),

    'cancel grandfather': frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/button/grandfathercc/cancel/0.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load( 'media/graphics/game/ui/button/grandfathercc/cancel/on.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load( 'media/graphics/game/ui/button/grandfathercc/cancel/c.png').convert_alpha(), 20)],
    ]),

    'battle map1': frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/game/battlemap/map_1.jpg').convert(), 1)]
    ]),

    'player plane lion': frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/planes/outlook/playerplane/lion/l1.png').convert_alpha(), 1),
        frame.FrameNum(pygame.image.load('media/graphics/planes/outlook/playerplane/lion/l2.png').convert_alpha(), 1),
        frame.FrameNum(pygame.image.load('media/graphics/planes/outlook/playerplane/lion/l3.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/planes/outlook/playerplane/lion/ord.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/planes/outlook/playerplane/lion/r1.png').convert_alpha(), 1),
        frame.FrameNum(pygame.image.load('media/graphics/planes/outlook/playerplane/lion/r2.png').convert_alpha(), 1),
        frame.FrameNum(pygame.image.load('media/graphics/planes/outlook/playerplane/lion/r3.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/planes/boom/player/boom1/1.png').convert_alpha(), 5),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/player/boom1/2.png').convert_alpha(), 5),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/player/boom1/3.png').convert_alpha(), 5),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/player/boom1/4.png').convert_alpha(), 5),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/player/boom1/5.png').convert_alpha(), 5),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/player/boom1/6.png').convert_alpha(), 5),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/player/boom1/7.png').convert_alpha(), 5),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/player/boom1/8.png').convert_alpha(), 5),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/player/boom1/9.png').convert_alpha(), 5),],
    ], leisureframe=1),
    'player plane bird': frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/planes/outlook/playerplane/bird/l1.png').convert_alpha(), 1),
         frame.FrameNum(pygame.image.load('media/graphics/planes/outlook/playerplane/bird/l2.png').convert_alpha(), 1),
         frame.FrameNum(pygame.image.load('media/graphics/planes/outlook/playerplane/bird/l3.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/planes/outlook/playerplane/bird/ord.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/planes/outlook/playerplane/bird/r1.png').convert_alpha(), 1),
         frame.FrameNum(pygame.image.load('media/graphics/planes/outlook/playerplane/bird/r2.png').convert_alpha(), 1),
         frame.FrameNum(pygame.image.load('media/graphics/planes/outlook/playerplane/bird/r3.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/planes/boom/player/boom1/1.png').convert_alpha(), 5),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/player/boom1/2.png').convert_alpha(), 5),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/player/boom1/3.png').convert_alpha(), 5),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/player/boom1/4.png').convert_alpha(), 5),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/player/boom1/5.png').convert_alpha(), 5),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/player/boom1/6.png').convert_alpha(), 5),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/player/boom1/7.png').convert_alpha(), 5),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/player/boom1/8.png').convert_alpha(), 5),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/player/boom1/9.png').convert_alpha(), 5), ],
    ], leisureframe=1),
    'playerhpframe': frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/planes/hp/frame/player/frame.png').convert_alpha(), 1)]
    ]),

    'playerhpbar': frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/planes/hp/bar/player/bar.png').convert_alpha(), 1)]
    ]),

    'player bullet red': frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/redweapon/red/red.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/redweapon/red/effect/1.png').convert_alpha(), 3),
        frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/redweapon/red/effect/2.png').convert_alpha(), 3),
        frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/redweapon/red/effect/3.png').convert_alpha(), 3),
        frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/redweapon/red/effect/4.png').convert_alpha(), 3),
        frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/redweapon/red/effect/5.png').convert_alpha(), 3),
        frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/redweapon/red/effect/6.png').convert_alpha(), 3)]
    ]),
    
    'player bullet redpoint':frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/redweapon/redpoint/redpoint.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/redweapon/red/effect/1.png').convert_alpha(), 3),
        frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/redweapon/red/effect/2.png').convert_alpha(), 3),
        frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/redweapon/red/effect/3.png').convert_alpha(), 3),
        frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/redweapon/red/effect/4.png').convert_alpha(), 3),
        frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/redweapon/red/effect/5.png').convert_alpha(), 3),
        frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/redweapon/red/effect/6.png').convert_alpha(), 3)]
    ]),
    
    'player bullet blue':frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/blueweapon/blue.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/blueweapon/effect/1.png').convert_alpha(), 3),
        frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/blueweapon/effect/2.png').convert_alpha(), 3),
        frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/blueweapon/effect/3.png').convert_alpha(), 3),
        frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/blueweapon/effect/4.png').convert_alpha(), 3)]
    ]),
    
    'player bullet bluepoint':frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/blueweapon/bluepoint.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/blueweapon/effect/1.png').convert_alpha(), 3),
        frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/blueweapon/effect/2.png').convert_alpha(), 3),
        frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/blueweapon/effect/3.png').convert_alpha(), 3),
        frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/playerplane/bullets/blueweapon/effect/4.png').convert_alpha(), 3)]
    ]),

    'sa_1': frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/planes/outlook/enemyplane/soldier/a-01/1.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/planes/boom/enemy/boom2/1.png').convert_alpha(), 3),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/enemy/boom2/2.png').convert_alpha(), 3),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/enemy/boom2/3.png').convert_alpha(), 3),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/enemy/boom2/4.png').convert_alpha(), 3),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/enemy/boom2/5.png').convert_alpha(), 3),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/enemy/boom2/6.png').convert_alpha(), 3),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/enemy/boom2/7.png').convert_alpha(), 3),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/enemy/boom2/8.png').convert_alpha(), 3),
         frame.FrameNum(pygame.image.load('media/graphics/planes/boom/enemy/boom2/9.png').convert_alpha(), 3), ]
    ], leisureframe=0),

    'sa_1 hpframe': frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/planes/hp/frame/enemy/frame.png').convert_alpha(), 1)]
    ]),

    'sa_1 hpbar': frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/planes/hp/bar/enemy/bar.png').convert_alpha(), 1)]
    ]),

    'sa_1 bullet': frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/enemyplane/bullet/red.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/enemyplane/bullet/effect/1.png').convert_alpha(), 1),
         frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/enemyplane/bullet/effect/2.png').convert_alpha(), 1),
         frame.FrameNum(pygame.image.load('media/graphics/planes/weapon/enemyplane/bullet/effect/3.png').convert_alpha(), 1)]
    ]),

    'grandfather bg': frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/game/bg/gramefatherbg/grandfatherbg.png').convert_alpha(), 1)]
    ]),

    'grandfather ui list': [
        frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/1/1.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/1/on.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/1/c.png').convert_alpha(), 1)]
    ]),

        frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/2/2.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/2/on.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/2/c.png').convert_alpha(), 1)]
    ]),

        frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/3/3.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/3/on.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/3/c.png').convert_alpha(), 1)]
    ]),
        frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/4/4.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/4/on.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/4/c.png').convert_alpha(), 1)]
    ]),
        frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/5/5.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/5/on.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/5/c.png').convert_alpha(), 1)]
    ]),
        frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/6/6.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/6/on.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/6/c.png').convert_alpha(), 1)]
    ]),

        frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/7/7.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/7/on.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/7/c.png').convert_alpha(), 1)]
    ]),

        frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/8/8.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/8/on.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/8/c.png').convert_alpha(), 1)]
    ]),

        frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/9/9.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/9/on.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/9/c.png').convert_alpha(), 1)]
    ]),

        frame.Frame(
    [
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/add/0.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/add/on.png').convert_alpha(), 1)],
        [frame.FrameNum(pygame.image.load('media/graphics/game/ui/grandfather_frames/add/c.png').convert_alpha(), 1)],
    ]),
    ]
}

 

