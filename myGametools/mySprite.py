import pygame
from myGametools import mymove, mypoint
from classes.media.frame.frame import Frame


class MySprite(pygame.sprite.Sprite):
    def __init__(self, frame: Frame, position):
        super().__init__()
        self.frame: Frame= frame
        self.image = self.frame.image
        self.rect = pygame.Rect(*position.position, *self.frame.image.get_size())

    def __getx(self):
        return self.rect.x
    def __setx(self, value):
        self.rect.x = value
    X = property(__getx, __setx)

    def __gety(self):
        return self.rect.y
    def __sety(self, value):
        self.rect.y = value
    Y = property(__gety, __sety)

    def __getpos(self):
        return self.rect.topleft
    def __setpos(self, pos):
        self.rect.topleft = pos
    position = property(__getpos, __setpos)

    def update(self) :
        self.frame.update()
        self.image = self.frame.image
        
    def draw(self, screen: pygame.Surface):
        screen.blit(self.frame.image, self.rect)

    def copy(self):
        return MySprite(self.frame.copy(), mypoint.Mypoint(self.rect.topleft))

class MyMoveSprite(MySprite):
    def __init__(self, frame, position, speed=None, accelerate=None):
        if speed is None:
            speed = [0, 0]
        if accelerate is None:
            accelerate = [0, 0]
        super().__init__(frame, position)
        mymove.Mymove.__init__(self, speed, accelerate)
    def move(self):
        self.X += self.speed[0]
        self.Y += self.speed[1]
        mymove.Mymove.updatespeed(self)
    def update(self) -> None:
        self.move()
        super().update()

    def copy(self):
        return MyMoveSprite(self.frame.copy(), mypoint.Mypoint(self.rect.topleft), self.speed, self.accelerate)