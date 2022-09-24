import pygame, random
from pygame.locals import *
from myGametools import mymove
from classes import boundlrtb, bound
from classes.planes import plane

class Engine(mymove.Mymove):
    # only for speed and accelerate(manally, just for player)
    # 目前在Engine类中硬编码所有飞船都应遵守的协议
    ACCE_x  = 1
    ACCE_y  = 0.2
    ACCE_F  = 0.5
    LEFT = 0
    LEISURE = 1
    RIGHT = 2
    STAGE_P = bound.BoundLineSymmetry([1, 4, 6, 10])
    (STAGE_LEFT3, STAGE_LEFT2, STAGE_LEFT1,
     STAGE_LEISURE,
     STAGE_RIGHT1, STAGE_RIGHT2, STAGE_RIGHT3) = (1, 2, 3,
                                                  4,
                                                  5, 6, 7)
    def __init__(self,  speedbound:boundlrtb.Boundlftb, speed=None, accelerate=None):
        super().__init__(speed, accelerate)
        self.speed_b = speedbound
        self.stage = self.STAGE_P.detect_section(self.speed[0])

    def w_acce(self):
        if self.speed_b.ylimit(self.speed[1]):
            if self.speed[1] > 0:
                self.setyAccelerate(-(self.ACCE_y + self.ACCE_F))
            else:
                self.setyAccelerate(-self.ACCE_y)

    def a_acce(self):
        if self.speed_b.xlimit(self.speed[0]):
            if self.speed[0] > 0:
                self.setxAccelerate(-(self.ACCE_x + self.ACCE_F))
            else:
                self.setxAccelerate(-self.ACCE_x)

    def s_acce(self):
        if self.speed_b.ylimit(self.speed[1]):
            if self.speed[1] < 0:
                self.setyAccelerate(self.ACCE_y + self.ACCE_F)
            else:
                self.setyAccelerate(self.ACCE_y)

    def d_acce(self):
        if self.speed_b.xlimit(self.speed[0]):
            if self.speed[0] < 0:
                self.setxAccelerate(self.ACCE_x + self.ACCE_F)
            else:
                self.setxAccelerate(self.ACCE_x)

    def drive(self):
        keys = pygame.key.get_pressed()
        if keys[K_w] and not keys[K_s]:
            self.w_acce()
        elif keys[K_s] and not keys[K_w]:
            self.s_acce()
        else:
            if self.accelerate[1]:
                self.accelerate[1] = 0
            if self.speed[1] > 0:
                self.speed[1] -= self.ACCE_F
                if self.speed[1] < 0:
                    self.speed[1] = 0
            elif self.speed[1] < 0:
                self.speed[1] += self.ACCE_F
                if self.speed[1] > 0:
                    self.speed[1] = 0
        if keys[K_a] and not keys[K_d]:
            self.a_acce()
        elif keys[K_d] and not keys[K_a]:
            self.d_acce()
        else:
            if self.accelerate[0]:
                self.accelerate[0] = 0
            if self.speed[0] > 0:
                self.speed[0] -= self.ACCE_F
                if self.speed[0] < 0:
                    self.speed[0] = 0
            elif self.speed[0] < 0:
                self.speed[0] += self.ACCE_F
                if self.speed[0] > 0:
                    self.speed[0] = 0
        self.updatespeed()
        self.updatestage()

    def updatestage(self):
        self.stage = self.STAGE_P.detect_section(self.speed[0])

    def updatespeed(self):
        self.speed[0] += self.accelerate[0]
        self.speed[1] += self.accelerate[1]
        self.speed[0] = self.speed_b.bound_1.setin(self.speed[0])
        self.speed[1] = self.speed_b.bound_2.setin(self.speed[1])

    def copy(self):
        return Engine(self.speed_b, self.speed[:], self.accelerate[:])


class Enemy_Engine(mymove.Mymove):
    def __init__(self):
        super().__init__()
        self.last_acce = pygame.time.get_ticks()
        self.acce_time = self.ACCE_TIME
        self.sleep_time = self.SLEEP_TIME
        self.sleeping = False
        self.acceing = False

    def copy(self):
        return Enemy_Engine()

class Sa_1_Engine(Enemy_Engine):
    ACCE_X = 1
    ACCE_Y = 0.1
    ACCE_F = 0.5
    ACCE_TIME = 300
    SLEEP_TIME = 100
    def drive(self):
        # 睡眠结束
        super().updatespeed()
        if not self.acceing and not self.sleeping:
            d = random.randint(1, 4)
            if d == 1:
                self.w_acce()
            if d == 2:
                self.a_acce()
            if d == 3:
                self.s_acce()
            if d == 4:
                self.d_acce()
            self.acceing = True
        # 加速中
        elif self.acceing and not self.sleeping:
            now = pygame.time.get_ticks()
            if now - self.last_acce >= self.ACCE_TIME:
                self.sleeping = True
                self.acceing = False
                self.accelerate = [0,0]
                self.last_acce = now
        # 睡眠中
        elif self.sleeping:
            if self.speed[0] > 0:
                self.speed[0] -= self.ACCE_F
                if self.speed[0] < 0:
                    self.speed[0] = 0
            elif self.speed[0] < 0:
                self.speed[0] += self.ACCE_F
                if self.speed[0] > 0:
                    self.speed[0] = 0
            if self.speed[1] > 0:
                self.speed[1] -= self.ACCE_F
                if self.speed[1] < 0:
                    self.speed[1] = 0
            elif self.speed[1] < 0:
                self.speed[1] += self.ACCE_F
                if self.speed[1] > 0:
                    self.speed[1] = 0
            now = pygame.time.get_ticks()
            if now - self.last_acce >= self.SLEEP_TIME:
                self.sleeping = False
                self.last_acce = now

    def w_acce(self):
        self.accelerate[1] = -self.ACCE_Y
    def a_acce(self):
        self.accelerate[0] = -self.ACCE_X
    def s_acce(self):
        # can use to drive show
        self.accelerate[1] = self.ACCE_Y
    def d_acce(self):
        self.accelerate[0] = self.ACCE_X

    def copy(self):
        return Sa_1_Engine()








