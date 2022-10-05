import random

from src import bound
from esign.tools.vector2 import Vector2

class Boundlftb:
    # 目前不支持改变
    def __init__(self, bound_x: bound.BoundUnit, bound_y: bound.BoundUnit):
        self.__left = bound_x[0]
        self.__right = bound_x[1]
        self.__top   = bound_y[0]
        self.__bottom = bound_y[1]
        self.__leftright = bound_x.room
        self.__topbottom = bound_y.room
        self.bound_x = bound_x
        self.bound_y = bound_y
        self.__bound = (self.bound_x, self.bound_y)

    @staticmethod
    def From(leftright: Vector2, bottomtop: Vector2):
        return Boundlftb(bound.BoundUnit(leftright.x, leftright.y), bound.BoundUnit(bottomtop.x, bottomtop.y))

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    @property
    def top(self):
        return self.__top

    @property
    def bottom(self):
        return self.__bottom

    @property
    def leftright(self):
        return self.__leftright

    @property
    def topbottom(self):
        return self.__topbottom

    @property
    def ymedium(self):
        return (self.__topbottom[0] + self.__topbottom[1]) / 2

    @property
    def xmedium(self):
        return (self.__leftright[0] + self.__leftright[1]) / 2

    @property
    def xlength(self):
        return self.__leftright[1] - self.__leftright[0]

    @property
    def ylength(self):
        return self.__topbottom[1] - self.__topbottom[0]

    def leftlimit(self, other, eq=True):
        return self.bound_x.floorlimit(other, eq)

    def rightlimit(self, other, eq=True):
        return self.bound_x.ceilinglimit(other, eq)

    def xlimit(self, other, eql=True, eqr=True):
        return self.bound_x.limit(other, eql, eqr)

    def toplimit(self, other, eq=True):
        return self.bound_y.floorlimit(other, eq)

    def bottomlimit(self, other, eq=True):
        return self.bound_y.ceilinglimit(other, eq)

    def ylimit(self, other, eqt=True, eqb=True):
        return self.bound_y.limit(other, eqt, eqb)

    def limit(self, x, y, xeqf=True, xeqc=True, yeqf=True, yeqc=True):
        return self.xlimit(x, xeqf, xeqc) and self.ylimit(y, yeqf, yeqc)

    def __getitem__(self, item):
        return self.__bound[item]

    def randompoint(self) -> Vector2:
        """
        生成在本范围内的随机点
        """
        x = random.random() * self.xlength + self.left
        y = random.random() * self.ylength + self.top
        return Vector2(x, y)

    def __and__(self, other):
        """
        求两个的交集
        """
        if self.ylimit(other.top) and not self.ylimit(other.bottom):
            if self.xlimit(other.left) and not self.xlimit(other.right):
                return Boundlftb.From(Vector2(other.left, self.right), Vector2(other.top, self.bottom))
            elif self.xlimit(other.right) and not self.xlimit(other.left):
                return Boundlftb.From(Vector2(self.left, other.right), Vector2(other.top, self.bottom))
            elif other.xlimit(self.right) and other.xlimit(self.left):
                return Boundlftb.From(Vector2(self.left, self.right), Vector2(other.top, self.bottom))
            elif self.xlimit(other.left) and self.xlimit(other.right):
                return Boundlftb.From(Vector2(other.left, other.right), Vector2(other.top, self.bottom))
        elif self.ylimit(other.bottom) and not self.ylimit(other.top):
            if self.xlimit(other.left) and not self.xlimit(other.right):
                return Boundlftb.From(Vector2(other.left, self.right), Vector2(self.top, other.bottom))
            elif self.xlimit(other.right) and not self.xlimit(other.left):
                return Boundlftb.From(Vector2(self.left, other.right), Vector2(self.top, other.bottom))
            elif other.xlimit(self.right) and other.xlimit(self.left):
                return Boundlftb.From(Vector2(self.left, self.right), Vector2(self.top, other.bottom))
            elif self.xlimit(other.left) and self.xlimit(other.right):
                return Boundlftb.From(Vector2(other.left, other.right), Vector2(self.top, other.bottom))
        elif self.ylimit(other.bottom) and self.ylimit(other.top):
            if self.xlimit(other.left) and not self.xlimit(other.right):
                return Boundlftb.From(Vector2(other.left, self.right), Vector2(other.top, other.bottom))
            elif self.xlimit(other.right) and not self.xlimit(other.left):
                return Boundlftb.From(Vector2(self.left, other.right), Vector2(other.top, other.bottom))
            elif other.xlimit(self.right) and other.xlimit(self.left):
                return Boundlftb.From(Vector2(self.left, self.right), Vector2(other.top, other.bottom))
            elif self.xlimit(other.left) and self.xlimit(other.right):
                return Boundlftb.From(Vector2(other.left, other.right), Vector2(other.top, other.bottom))
        elif other.ylimit(self.top) and other.ylimit(self.bottom):
            if self.xlimit(other.left) and not self.xlimit(other.right):
                return Boundlftb.From(Vector2(other.left, self.right), Vector2(self.top, self.bottom))
            elif self.xlimit(other.right) and not self.xlimit(other.left):
                return Boundlftb.From(Vector2(self.left, other.right), Vector2(self.top, self.bottom))
            elif other.xlimit(self.right) and other.xlimit(self.left):
                return Boundlftb.From(Vector2(self.left, self.right), Vector2(self.top, self.bottom))
            elif self.xlimit(other.left) and self.xlimit(other.right):
                return Boundlftb.From(Vector2(other.left, other.right), Vector2(self.top, self.bottom))
        else:
            return None