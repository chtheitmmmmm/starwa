import math

from .statemachine import stateDefine

@stateDefine('first', 'second', 'end')
class _VectorIterator:
    def __init__(self, v):
        self.v = v
        self.switch('first')

    def __iter__(self):
        return self

    def __next__(self):
        if self.state == self.first:
            self.switch('second')
            return self.v.x
        elif self.state == self.second:
            self.switch('end')
            return self.v.y
        else:
            raise StopIteration()

class Vector2:

    __slots__ = ['x', 'y']
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @staticmethod
    def From(iterable):
        """
        从一个可迭代对象产生 Vector
        """
        return Vector2(*(i for i in iterable))

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __mul__(self, times: float):
        return Vector2(self.x * times, self.y * times)
    def __imul__(self, times):
        self.x *= times
        self.y *= times
        return self

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __getitem__(self, item):
        if item == 0 or item == -2:
            return self.x
        elif item == 1 or item == -1:
            return self.y
        else:
            raise IndexError('下标越界！')

    def __setitem__(self, key, value):
        if key == 0 or key == -2:
            self.x = value
        elif key == 1 or key == -1:
            self.y = value
        else:
            raise IndexError('下标越界！')

    def __str__(self):
        return f'<{self.x}, {self.y}>'

    def __iter__(self):
        """
        可迭代支持
        """
        return _VectorIterator(self)

    @property
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def copy(self):
        return Vector2(self.x, self.y)


__all__ = ['Vector2']