import pygame
from . import button

class Menu_Buttons(pygame.sprite.Group):
    def __init__(self, read_grandfather:button.Button):
        super().__init__(read_grandfather)
        self.read_grandfather = read_grandfather
    def recover(self):
        for i in self.sprites():
            i.recover()

class con_can_grand(pygame.sprite.Group):
    def __init__(self, confirm:button.Button, cancel:button.Button):
        super().__init__(confirm, cancel)
        self.confirm = confirm
        self.cancel = cancel

    def recover(self):
        for i in self.sprites():
            i.recover()






