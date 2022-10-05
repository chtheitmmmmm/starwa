import pygame

STICKS1  = 1
NOTSTICK = 0
STICKS2  = -1

def midalign_vertical(s1:pygame.sprite.Sprite, s2:pygame.sprite.Sprite, stickS1flag:int=0) -> None:
    "垂直对齐两个Sprite"
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

def midalign_verticalItem(screen: pygame.Surface, item: pygame.sprite.Sprite):
    item.rect.centerx = screen.get_rect().centerx

def midalign_horizental(s1:pygame.sprite.Sprite, s2:pygame.sprite.Sprite, stickS1flag:int=0) -> None:
    "水平对齐两个Sprite"
    if stickS1flag == STICKS1:
        s2.rect.centery = s1.rect.centery
    elif stickS1flag == STICKS2:
        midalign_horizental(s2, s1, STICKS1)
    elif stickS1flag == NOTSTICK:
        newcentery = (s1.rect.centery + s2.rect.centery) / 2
        s1.rect.centery = newcentery
        s2.rect.centery = newcentery
    else:
        raise ValueError('stickflag not in 1, -1, 0')

def midalign_horizentalItem(screen: pygame.Surface, item: pygame.sprite.Sprite):
    item.rect.centery = screen.get_rect().centery

def midalign(s1:pygame.sprite.Sprite | pygame.Surface, s2:pygame.sprite.Sprite | pygame.Surface, stickS1flag:int=0) -> None:
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

def midalignItem(screen: pygame.Surface, item: pygame.sprite.Sprite):
    item.rect.center = screen.get_rect().center

__all__ = [
    'midalignItem'          , 'midalign',
    'midalign_horizental'   , 'midalign_horizentalItem',
    'midalign_vertical'     , 'midalign_verticalItem',
    'STICKS1', 'STICKS2'    , 'NOTSTICK',
]