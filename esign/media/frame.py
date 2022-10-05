import pygame
import copy

class FrameSingle:
    """
    虚帧优化，用于传给FrameGroup构造函数
    """
    __slots__ = ['__image', '__num']
    def __init__(self, frame:pygame.Surface, num:int):
        self.__image = frame
        self.__num   = num

    def __getnum(self):
        return self.__num
    def __setnum(self, other):
        self.__num = other
    num = property(__getnum)

    def __getimg(self):
        return self.__image
    image = property(__getimg)

    def __mul__(self, other):
        self.__num *= other
        return self

    def __imul__(self, other):
        self.__num *= other
        return self

    def __getitem__(self, item):
        if item == 0:
            return self.image
        elif item == 1:
            return self.num
        else:
            raise ValueError('indexvalue not 0 or 1!')

    def last(self, num: int):
        return num >= self.__num

    def __deepcopy__(self, memodict={}):
        return self

class FrameGroup(list):
    """
    用于传给Action构造函数
    :param frames: 一组FrameSingle的列表
    """
    __slots__ = ['__exhaust', '__current', '__step']
    def __init__(self, frames: list[FrameSingle]):
        super(FrameGroup, self).__init__(frames)
        self.resume()

    def resume(self):
        self.__exhaust = False                    # 该动作的帧是否跑完
        self.__current = 0                        # 该动作的当前帧
        self.__step = 0                           # 该动作的当前帧的消耗量

    def getCurrentFrameSingle(self) -> FrameSingle:
        return self[self.__current]

    def getCurrentImage(self):
        return self.getCurrentFrameSingle().image

    def lastStep(self):
        """
        当前step是否为该帧最后一个虚帧
        """
        return self.getCurrentFrameSingle().last(self.__step)

    def lastFrame(self):
        """
        当前帧是否为最后一帧，判断是否耗尽请使用exhaust()
        """
        return self.__current == len(self) - 1

    def exhaust(self):
        return self.__exhaust

    def go(self):
        """
        返回是否耗尽
        """
        if self.lastStep():
            if self.lastFrame():
                self.__exhaust = True
                return True
            else:
                self.__current += 1
                self.__step = 1
        else:
            self.__step += 1
        return False

class FramePool(dict):
    """
    帧池，用于管理所有复用帧
    """
    def __init__(self, graphicRoot:str):
        """
        :param graphicRoot: 根目录，将会自动扫描里面所有图片文件并生成字典。
        """
        self.root = graphicRoot

    def registers(self, finders: dict):
        """
        nameitem: {
            name1: [
                { filename1: num },
                { filename2: num },
                { filename3: num }
            ],
            name2: {
                name21: [
                    { filename4: num },
                    { filename5: num },
                    { filename6: num }
                ]
                name22: [
                    { filename: num },
                    { filename: nameitem }
                ]
            }
        }
        """
        path = self
        queue = [(path, finders)]        # 广搜队列
        while queue:
            p, v = queue.pop(0)
            for n in v:
                if isinstance(v[n], list):
                    framenums = []
                    for framesingle in v[n]:
                        assert len(framesingle) == 1
                        fs = [fs for fs in framesingle.items()][0]
                        framenums.append(
                            FrameSingle(pygame.image.load(f'{self.root}/{fs[0]}').convert_alpha(), fs[1])
                        )
                    p[n] = framenums    # 保存复用 FrameNum对象
                elif isinstance(v[n], dict):
                    queue.append((p.setdefault(n, v[n]),v[n]))
                else:
                    raise TypeError("dict or list is only expected.")

    def bail(self, *wraperPath): # 从水池中舀水，返回dict或FrameNum列表或自身或直接报错
        if len(wraperPath):
            assert all([isinstance(item, str) for item in wraperPath])
            r = self
            for i in wraperPath:
                r = r[i]
            return r
        else:
            return self

__all__ = ['FrameSingle', 'FrameGroup', 'FramePool']