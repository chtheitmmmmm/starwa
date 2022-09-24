import pygame

STICKS1  = 1
NOTSTICK = 0
STICKS2  = -1

def midalign_vertical(s1:pygame.sprite.Sprite, s2:pygame.sprite.Sprite, stickS1flag:int=0) -> None:
    "垂直对齐两个Surface"
    if stickS1flag == STICKS1:
        s2.rect.centerx = s1.rect.centerx
    elif stickS1flag == STICKS2:
        midalign_vertical(s2, s1, STICKS1)
    elif stickS1flag == NOTSTICK:
        newcenterx = (s1.rect.centerx + s2.rect.centerx) / 2
        s1.rect.centerx = newcenterx
        s2.rect.centerx = newcenterx
    else:
        raise ValueError('stickflag not in 1, -1, 0')

def midalign_level(s1:pygame.sprite.Sprite, s2:pygame.sprite.Sprite, stickS1flag:int=0) -> None:
    "水平对齐两个Surface"
    if stickS1flag == STICKS1:
        s2.rect.centery = s1.rect.centery
    elif stickS1flag == STICKS2:
        midalign_level(s2, s1, STICKS1)
    elif stickS1flag == NOTSTICK:
        newcentery = (s1.rect.centery + s2.rect.centery) / 2
        s1.rect.centery = newcentery
        s2.rect.centery = newcentery
    else:
        raise ValueError('stickflag not in 1, -1, 0')

def midalign(s1:pygame.sprite.Sprite, s2:pygame.sprite.Sprite, stickS1flag:int=0) -> None:
    '居中对齐两个Surface对象'
    if stickS1flag == STICKS1:
        s2.rect.center = s1.rect.center
    elif stickS1flag == STICKS2:
        midalign(s2, s1, STICKS1)
    elif stickS1flag == NOTSTICK:
        newcenter = (
            (s1.rect.centerx + s2.rect.centerx) / 2,
            (s1.rect.centery + s2.rect.centery) / 2,
        )
        s1.rect.center = newcenter
        s2.rect.center = newcenter
    else:
        raise ValueError('stickflag not in 1, -1, 0')
