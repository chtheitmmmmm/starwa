
import pygame

def selfadaptleft(s:pygame.sprite.Sprite, screen:pygame.Surface):
    if s.rect.height == screen.get_height():
        return
    hi  =  screen.get_height()
    we  =  s.rect.width / s.rect.height * hi
    s.frame.image = pygame.transform.smoothscale(s.frame.image, (we, hi))
    s.rect = s.frame.image.get_rect()

def selfadapttop(s:pygame.sprite.Sprite, screen:pygame.Surface):
    if s.rect.width == screen.get_width():
        return
    we  = screen.get_width()
    hi  = s.rect.height / s.rect.width * we
    s.frame.image = pygame.transform.smoothscale(s.frame.image, (we, hi))
    s.rect  = s.frame.image.get_rect()

