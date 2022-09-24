import random

import pygame
from . import engine
from classes import bound, boundlrtb
from init import constants
from init import globalsInit

class ControlCenter:
    '''
    manage move and location
    '''
    def __init__(self, engine:engine.Engine):
        # engine only manage speed changing and accelerate changing
        self.engine = engine
        # 预加载screen_bound 免得每次都重复生成
        self.space_b = globalsInit.screen_bound

    def configure(self, plane):
        # 初始位置
        self.plane = plane
        self.rect = pygame.Rect(
            int(constants.SCREEN_SIZE[0] / 2 - plane.rect.width),
            int(constants.BeginLocCEnter - plane.rect.height / 2),
            plane.rect.width,
            plane.rect.height
        )
        plane.rect = self.rect

    def control(self):
        self.engine.drive()
        self.updatelocation()
        self.plane.rect = self.rect

    def updatelocation(self):
        if not self.space_b.leftlimit(self.rect.left, True):
            self.rect.left = self.space_b.left
        elif not self.space_b.rightlimit(self.rect.right, True):
            self.rect.right = self.space_b.right
        if not self.space_b.toplimit(self.rect.top, True):
            self.rect.top = self.space_b.top
        elif not self.space_b.bottomlimit(self.rect.bottom, True):
            self.rect.bottom = self.space_b.bottom
        self.rect.left += self.engine.speed[0]
        self.rect.top += self.engine.speed[1]

    def copy(self):
        return ControlCenter(self.engine.copy())

class Enemy_Controlcenter(ControlCenter):
    def configure(self, plane):
        self.plane = plane
        self.rect = plane.rect

class Sa_1_Controlcenter(Enemy_Controlcenter):
    def control(self):
        if self.rect.bottom < 0:
            self.engine.a_acce()
        else:
            super().control()





