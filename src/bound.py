import pygame

import sys
# bound族都有limit协议

class BoundUnit:
    NEGATIVE_INFINITY = b'\x11'
    POSITIVE_INFINITY = b'\x01'
    def __init__(self, floor=NEGATIVE_INFINITY, ceiling=POSITIVE_INFINITY):
        self.__floor = floor
        self.__ceiling = ceiling
        self.__room = (floor, ceiling)

    @property
    def floor(self):
        return self.__floor

    @property
    def ceiling(self):
        return self.__ceiling

    @property
    def room(self):
        return self.__room

    def floorlimit(self, other, eq=True):
        if self.floor == self.NEGATIVE_INFINITY:
            return True
        if eq:
            return self.floor <= other
        else:
            return self.floor < other

    def ceilinglimit(self, other, eq=True):
        if self.ceiling == self.POSITIVE_INFINITY:
            return True
        if eq:
            return other <= self.ceiling
        else:
            return other < self.ceiling

    def limit(self, other, eqf=True, eqc=True):
        return self.floorlimit(other, eqf) and self.ceilinglimit(other, eqc)

    def setin(self, other, eqf=True, eqc=True):
        if not self.floorlimit(other, eqf):
            other = self.floor
        elif not self.ceilinglimit(other,eqc):
            other = self.ceiling
        return other

    def __getitem__(self, item):
        return self.room[item]


class BoundGroup:
    # 限制群
    def __init__(self, *groups):
        self.bounds = set(groups)

    def __add__(self, other):
        return self.bounds + other.bounds

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.bounds += set(other)
        return self

    def limit(self, other):
        for i in self.bounds:
            if not i.limit(other):
                return False
        return True


class BoundLine:
    # 切割数轴的有序bound
    # 必须为升序
    def __init__(self, boundpoints):
        bounds = []
        self.boundlen = len(boundpoints) + 1
        if self.boundlen  == 1:
            bounds.append(BoundUnit(BoundUnit.NEGATIVE_INFINITY, BoundUnit.POSITIVE_INFINITY))
        else:
            bounds.append(BoundUnit(BoundUnit.NEGATIVE_INFINITY, boundpoints[0]))
            for i in range(self.boundlen-2):
                if not boundpoints[i] < boundpoints[i+1]:
                    raise ValueError('please garantee its ascending order')
                bounds.append(BoundUnit(boundpoints[i], boundpoints[i+1]))
            bounds.append(BoundUnit(boundpoints[-1], BoundUnit.POSITIVE_INFINITY))
        self.bounds = bounds

    def detect_section(self, other, righteq=True):
        for i in range(self.boundlen):
            if self.bounds[i].limit(other, not righteq, righteq):
                return i


class BoundLineSymmetry(BoundLine):
    def __init__(self, boundpoints):
        """
        :param boundpoints: 升序列表
        """
        bounds = []
        boundpoints.reverse()
        negboundpoints = [-i for i in boundpoints]
        self.lefthalfbounds = BoundLine(negboundpoints)
        for i in negboundpoints:
            bounds.append(i)
        boundpoints.reverse()
        self.righthalfbounds  = BoundLine(boundpoints)
        if boundpoints[0]:
            bounds.append(boundpoints[0])
        for i in boundpoints[1:]:
            bounds.append(i)
        super().__init__(bounds)

    def detect_section(self, other, righteq=True):
        leftdetect = self.lefthalfbounds.detect_section(other, not righteq)
        rightdetect = self.righthalfbounds.detect_section(other, righteq)
        return leftdetect + rightdetect


