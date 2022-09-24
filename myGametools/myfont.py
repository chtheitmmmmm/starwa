#
# Created by 程闽 on 2022/01/21
#

import pygame

class Myfont:
    def __init__(self, screen:pygame.Surface, position, size, color, content, backgruond=None, type_f=None):
        self.screen   = screen
        self.position = position
        self.content = content
        self.color = color
        self.size = size
        self.bg    = backgruond
        self.type_f = type_f
        self.font = pygame.font.Font(None, int(size))
        self.surface = self.font.render(content, True, color, backgruond)

    def show(self):
        return self.screen.blit(self.surface, self.position)

class Myfont2:
    def __init__(self, screen:pygame.Surface, position, size, color,backgruond=None, type_f=None):
        self.screen   = screen
        self.position = position
        self.color = color
        self.size = size
        self.bg    = backgruond
        self.type_f = type_f
        self.font = pygame.font.Font(None, int(size))


    def show(self, content):
        surface = self.font.render(content, True, self.color, self.bg)
        return self.screen.blit(surface, self.position)
