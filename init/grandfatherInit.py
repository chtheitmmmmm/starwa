import shelve, pygame
import sys

from classes import boundlrtb
from myGametools import mypoint
from init import constants, graphicsInit, audioInit
from classes.buttons import button



class Grandfathers(pygame.sprite.Group):
    def __init__(self, bound:boundlrtb.Boundlftb):
        super().__init__()
        self.bound = bound
        file = shelve.open('database/player_data')
        self.grand_num = file['']
        self.grands = []
        for i in range(self.grand_num):
            self.grands.append(
                button.Button(graphicsInit.alls['grandfather ui list'][i],
                              audioInit.grandfather_frame,
                              mypoint.Mypoint((self.bound.left, self.bound.top+i*constants.GRAND_SIZE[1]))
                )
            )
        if self.grand_num < constants.GRAND_NUM_MAX:
            self.grands.append(
                button.Button(graphicsInit.alls['grandfather ui list'][constants.GRAND_NUM_MAX],
                              audioInit.grandfather_frame,
                              mypoint.Mypoint((self.bound.left, self.bound.top+(self.grand_num-1)*constants.GRAND_SIZE[1]))
                )
            )
        self.grand_num = len(self.grands)
        self.loc = mypoint.Mypoint((bound.left, bound.top))
        self.update_num()
        file.close()

    def update_num(self) -> None:
        self.firstnum = (self.loc.Y - self.bound.top) // constants.GRAND_SIZE[1]
        self.lastnum = (self.bound.bottom - self.bound.top) // constants.GRAND_SIZE[1] + self.firstnum + 1
        self.lastnum = self.lastnum if self.lastnum < self.grand_num else self.grand_num-1

    def update(self):
        self.update_num()
        print(self.firstnum, self.lastnum)
        for i in range(self.firstnum):
            self.grands[i].rect.top = self.loc.Y + i * constants.GRAND_SIZE[1]
        for i in range(self.firstnum, self.lastnum+1):
            self.grands[i].update()
            self.grands[i].rect.top = self.loc.Y + i * constants.GRAND_SIZE[1]
        for i in range(self.lastnum+1, self.grand_num):
            self.grands[i].rect.top = self.loc.Y + i * constants.GRAND_SIZE[1]

    def draw(self, screen:pygame.Surface):
        difference = self.loc.Y - self.bound.top
        hidelenup = constants.GRAND_SIZE[1] - (difference-difference//constants.GRAND_SIZE[1])
        dislendown = self.bound.bottom - (self.bound.top - hidelenup + (self.lastnum - self.firstnum)*constants.GRAND_SIZE[1])
        if self.grand_num > 1:
            screen.blit(
                self.grands[self.firstnum].image,
                (self.bound.left, self.bound.top),
                (0, hidelenup, constants.GRAND_SIZE[0], constants.GRAND_SIZE[1]-hidelenup))
        for i in range(self.firstnum+1, self.lastnum):
            screen.blit(
            self.grands[i].image,
            (self.bound.left, self.bound.top + (i-self.num+1)*constants.GRAND_SIZE[1])
        )
        screen.blit(
            self.grands[self.lastnum].image,
            (self.bound.left, self.bound.top+self.lastnum*constants.GRAND_SIZE[1]),
            (0, 0, constants.GRAND_SIZE[0], dislendown)
        )

    def roll(self, mouse_wheel):
        if self.lastnum - self.firstnum >= 4:
            if mouse_wheel.y > 0:
                if not self.bound.toplimit(
                    self.loc.Y + mouse_wheel.y,
                    False
            ) :
                    self.loc.Y += mouse_wheel.y


            else :
                if not self.bound.bottomlimit(
                self.loc.Y + (self.lastnum + 1)*constants.GRAND_SIZE[1]
            ) :
                    self.loc.Y += mouse_wheel.y
                    self.loc.Y = self.bound.top





