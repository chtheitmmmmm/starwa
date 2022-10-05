import pygame
from esign.item import Item, MovableItem
from esign.tools.selfAdapt import selfadapttop
from esign.tools.vector2 import Vector2

class VerticalBG(MovableItem):

    def draw(self, screen: pygame.Surface):
        super(VerticalBG, self).draw(screen)
        if self.rect.top <= screen.get_height():
            screen.blit(self.image, (0, self.rect.top - self.rect.height))
        elif self.rect.top > screen.get_height():
            self.pos = Vector2(0, screen.get_height() - self.rect.height)

    def copy(self):
        return VerticalBG(
            media=self.media,
            pos = self.pos,
            speed = self.speed
        )
__all__ = ["VerticalBG"]