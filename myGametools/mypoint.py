import random
import pygame
from . import mymove


class Mypoint:
    '''
    a common point

    '''
    def __init__(self, position=None):
        if position is None:
            position=[0,0]
        self.__position = list(position)
    def __getx(self):
        return self.__position[0]
    def __setx(self, other):
        self.__position[0] = other
    X = property(__getx, __setx)
    def __gety(self):
        return self.__position[1]
    def __sety(self, other):
        self.__position[1] = other
    Y = property(__gety, __sety)
    def __getpos(self):
        return self.__position
    def __setpos(self, other:list):
        self.__position = other
    position = property(__getpos, __setpos)

    def __getitem__(self, item):
        return self.__position[item]

class MyMovePoint(mymove.Mymove, Mypoint):
    '''
    inherit:
    Mypoint.getposition
    Mymove.setAccelerate
    Attribute:
        position list[,]
        speed
    '''
    def __init__(self, position=None, speed=None, accelerate=None):
        if position is None:
            position = [0, 0]
        if accelerate is None:
            accelerate = [0, 0]
        if speed is None:
            speed = [0, 0]
        self.position = list(position)
        self.item = Mypoint((position[0],position[1]))
        self.speed = list(speed)
        self.accelerate = list(accelerate)
    def move(self):
        '''
        move the point and update its accelerate
        :return:
        '''
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]
        self.updateAccelerate()


def randPoint(surface:pygame.Surface):
    return Mypoint((random.random()*surface.get_width(), random.random()*surface.get_height()))


