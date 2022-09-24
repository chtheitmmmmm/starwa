import shelve
import pygame

class Grandfather:
    def __init__(self):
        '''
        raise ValueError if player's name longer than 20,
         else if name has been used,
         elif grandfather's number has upper than 90
        :param name:
        '''
        # if 0 < len(name) < 20:
        #     raise ValueError('名字长度应不小于1且不大于20！')
        file = shelve.open('database/player_data')
        # if name in file:
        #     raise ValueError('存档命名已被使用！')
        # number = file[''] + 1
        # if number > 9:
        #     raise ValueError('存档数已满，请尝试删除一个已有存档！')
        # file[''] = number
        # self.name = name
        self.gold_num = 0
        self.number = number
        file[self.name] = self
        file.close()

    def __del__(self):
        file = shelve.open('database/player_data')
        file[self.name] = self
        file.close()

