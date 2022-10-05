import pygame

from esign import *
from .player.playerplane import PlayerPlane
import random

class Character:
    """
    角色，有一个名称，一个人物形象，一些语录
    """
    def __init__(self, name: str, nameitem: Item, people: Item, sentences: list[Audio], plane: PlayerPlane):
        self.name = name
        self.nameitem = nameitem
        self.people = people
        self.sentences = sentences
        self.plane = plane

    def randomsay(self):
        random.choice(self.sentences).play()

    def show(self):
        self.nameitem.action(ORD)
        self.people.action(ORD)
        self.randomsay()

    def draw(self, screen: pygame.Surface):
        self.nameitem.draw(screen)
        self.people.draw(screen)
        screen.blit(self.plane.image, self.plane.rect)

    def update(self):
        self.nameitem.update()
        self.people.update()
        self.plane.update(None)


class CharcterGroup(list):
    def __init__(self, charcters: list, crt: int=0):
        super(CharcterGroup, self).__init__(charcters)
        self[crt]
        self.crt = crt

    @property
    def character(self):
        return self[self.crt]

    def switchCharacter(self, idx: int):
        self[idx]
        for s in self.character.sentences:
            s.stop()
        self.crt = idx
        self.character.show()

    def switchNextCharacter(self):
        self.switchCharacter(self.crt + 1)

    def switchLastCharacter(self):
        self.switchCharacter(self.crt - 1)

    def draw(self, screen: pygame.Surface):
        self.character.draw(screen)

    def update(self):
        self.charcter.update()

__all__ = ['CharcterGroup', 'Character']


