import pygame
from esign import *
from src.msg import *
from .enemyplane import *

class Enemy:
    """
    used for remote enemy.
    """
    def __init__(self, id: float, enemytype: type, pos: Vector2):
        self.id = id
        self.plane = enemytype(Vector2(*pos))

    def draw(self, screen: pygame.Surface):
        self.plane.draw(screen)

    def update(self, enemy_group):
        self.plane.update(enemy_group)


__all__ = ['Enemy']