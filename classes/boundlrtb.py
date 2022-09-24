from classes import bound


class Boundlftb:
    # 目前不支持改变
    def __init__(self, bound_1: bound.BoundUnit, bound_2: bound.BoundUnit):
        self.__left = bound_1[0]
        self.__right = bound_1[1]
        self.__top   = bound_2[0]
        self.__bottom = bound_2[1]
        self.__leftright = bound_1.room
        self.__topbottom = bound_2.room
        self.bound_1 = bound_1
        self.bound_2 = bound_2
        self.__bound = (self.bound_1, self.bound_2)

    def __getl(self):
        return self.__left

    def __getr(self):
        return self.__right

    def __gett(self):
        return self.__top

    def __getb(self):
        return self.__bottom

    def __getlr(self):
        return self.__leftright

    def __gettb(self):
        return self.__topbottom

    left = property(__getl)
    right = property(__getr)
    top = property(__gett)
    bottom = property(__getb)
    leftright = property(__getlr)
    topbottom = property(__gettb)

    def leftlimit(self, other, eq=True):
        return self.bound_1.floorlimit(other, eq)

    def rightlimit(self, other, eq=True):
        return self.bound_1.ceilinglimit(other, eq)

    def xlimit(self, other, eql=True, eqr=True):
        return self.bound_1.limit(other, eql, eqr)

    def toplimit(self, other, eq=True):
        return self.bound_2.floorlimit(other, eq)

    def bottomlimit(self, other, eq=True):
        return self.bound_2.ceilinglimit(other, eq)

    def ylimit(self, other, eqt=True, eqb=True):
        return self.bound_2.limit(other, eqt, eqb)

    def limit(self, x, y, xeqf=True, xeqc=True, yeqf=True, yeqc=True):
        return self.xlimit(x, xeqf, xeqc) and self.ylimit(y, yeqf, yeqc)

    def __getitem__(self, item):
        return self.__bound[item]