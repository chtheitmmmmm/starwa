import pygame

SMOOTH_SCALE = b'0x01'
SCALE        = b'0x02'

def selfadaptleft(s, screen:pygame.Surface, method=SMOOTH_SCALE):
    """
    s should be transformalbe item
    adapt height side, won't stretch
    """
    if method != SMOOTH_SCALE and method != SCALE:
        raise ValueError('The method not support!')
    if s.rect.height == screen.get_height():
        return
    v = screen.get_height() / s.rect.height
    if method == SMOOTH_SCALE:
        s.smoothscale((s.rect.width * v, s.rect.height * v))
    else:
        s.scale((s.rect.width * v, s.rect.h * v))

def selfadapttop(s, screen:pygame.Surface, method=SMOOTH_SCALE):
    """
    s should be transformalbe item
    adapt width size. won't stretch
    """
    if method != SMOOTH_SCALE and method != SCALE:
        raise ValueError('The method not support!')
    if s.rect.height == screen.get_height():
        return
    v = screen.get_width() / s.rect.width
    if method == SMOOTH_SCALE:
        s.smoothscale((s.rect.width * v, s.rect.height * v))
    else:
        s.scale((s.rect.width * v, s.rect.h * v))

def selfadapt(s, screen: pygame.Surface, method=SMOOTH_SCALE):
    """
    s should be transformalbe item
    adapt both size. may cause a stretching
    """
    if method != SMOOTH_SCALE and method != SCALE:
        raise ValueError('The method not support!')
    if s.rect.height == screen.get_height() and s.rect.width == screen.get_width():
        return
    if method == SMOOTH_SCALE:
        s.smoothscale((screen.get_width(), screen.get_height()))
    else:
        s.scale((screen.get_width(), screen.get_height()))

__all__ = ['selfadapt', 'selfadapttop', 'selfadaptleft', "SMOOTH_SCALE", 'SCALE']