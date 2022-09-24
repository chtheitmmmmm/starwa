class Mymove:
    '''
    need the item has x and y attribute
    '''
    def __init__(self, speed:list=None, accelerate:list=None):
        '''
        :param speed: move speed (vx, vy)
        :param accelerate: moveaccelerate(ax, ay)
        '''
        if accelerate is None:
            accelerate = [0, 0]
        if speed is None:
            speed = [0,0]
        self.speed = list(speed)
        self.accelerate = list(accelerate)
    def setAccelerate(self, ac_x=0, ac_y=0):
        '''
        to set the move object
        :param ac_x: one in one out function
        :param ac_y: one in one out function
        :return: new accelerate
        '''
        self.accelerate = [ac_x, ac_y]
    def updatespeed(self):
        self.speed[0] += self.accelerate[0]
        self.speed[1] += self.accelerate[1]

    def setxAccelerate(self, vx):
        self.accelerate[0] = vx

    def setyAccelerate(self, vy):
        self.accelerate[1] = vy


