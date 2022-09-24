import pygame

class FrameNum:
    def __init__(self, frame:pygame.Surface, num:int):
        self.image = frame
        self.num   = num
    def __getframe(self):
        return self.__frame
    def __setframe(self, other):
        self.__frame = other
    frame = property(__getframe, __setframe)

    def __getnum(self):
        return self.__num
    def __setnum(self, other):
        self.__num = other
    num = property(__getnum, __setnum)

    def __mul__(self, other):
        self.num *= other
        return self

    def __imul__(self, other):
        self.num *= other
        return self

    def __getitem__(self, item):
        if item == 0:
            return self.image
        elif item == 1:
            return self.num
        else:
            raise ValueError('indexvalue not 0 or 1!')


class Frame:
    'like [[(frame1,num1),(frame2,num2)],[...]]'
    LASTCIRCLE= b'\x01'
    LASTSTICK = b'\x00'
    def __init__(self, framelist, leisureframe=0):
        self.framelist  = framelist
        # this condition
        self.this_code  = leisureframe
        self.thiscondition = framelist[self.this_code]
        # this condition len
        self.thiscdlen  = len(self.thiscondition)
        # this frame
        self.thisframe  = 0
        # this frame num
        self.thisfnum   = self.thiscondition[self.thisframe][1]
        self.thisgone   = 0
        self.image      = self.thiscondition[self.thisframe][0]
        self.next_code  = self.LASTCIRCLE
        self.sticked    = False
        # 得到本状态的虚拟帧数目

        self.leisureframe = leisureframe
    def set_stick(self):
        self.next_code = self.LASTSTICK
    def unsetonce(self):
        self.next_code = self.LASTCIRCLE

    def update(self):
        # 若为循环播放
        if not self.sticked:
            if self.next_code == self.LASTCIRCLE:
                self.circleupdate()
            elif self.next_code == self.LASTSTICK:
                self.stickupdate()
            else:
                self.onceupdate()

    def changecondition(self, condition_code):
        self.thiscondition = self.framelist[condition_code]
        self.thisgone   = 0
        self.thisframe  = 0
        self.this_code = condition_code
        self.thiscdlen  = len(self.thiscondition)
        self.updateframe()
    # 跳转condition代码
    def set_next(self, next_code):
        self.next_code = next_code

    def set_condition(self, this_code):
        self.this_code = this_code
    
    def circleupdate(self):
        # 若达到这一帧的最后一个
        if self.thisgone >= self.thisfnum:
            # 进入下一帧
            self.nextframe()
            # 若超过最后一帧
            if self.thisframe >= self.thiscdlen:
                self.thisframe = 0
                self.thisgone = 0
            # 图像变化
            self.updateframe()
        # 下一个虚帧
        self.go()
        
    def stickupdate(self):
        if self.thisframe < self.thiscdlen - 1:
            if self.thisgone >= self.thisfnum - 1:
                self.nextframe()
                self.updateframe()
            else:
                self.go()
        elif self.thisframe == self.thiscdlen - 1:
            if self.thisgone < self.thisfnum - 1:
                self.go()
            else:
                if not self.sticked:
                    self.sticked = True

    def onceupdate(self):
        if not self.thisframe == self.next_code:
            if self.thisframe < self.thiscdlen - 1:
                if self.thisgone >= self.thisfnum:
                    self.nextframe()
                    self.updateframe()
                self.go()
            else:
                if self.thisgone >= self.thisfnum:
                    self.changecondition(self.next_code)
                else:
                    self.go()
    def set_certain(self, new_thisframe, new_condition_code, sticked=False):
        self.this_code = new_condition_code
        self.thisframe = new_thisframe
        self.thiscondition = self.framelist[self.this_code]
        self.updateframe()
        self.thiscdlen = len(self.thiscondition)
        self.thisgone = 0
        self.next_code = self.LASTSTICK if sticked else self.LASTCIRCLE
        self.sticked = False

    def nextframe(self):
        self.thisgone = 0
        self.thisframe += 1

    def updateframe(self):
        self.image = self.thiscondition[self.thisframe][0]
        self.thisfnum = self.thiscondition[self.thisframe][1]

    def go(self):
        self.thisgone += 1

    def copy(self):
        return Frame(self.framelist, self.leisureframe)







