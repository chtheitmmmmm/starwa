import pygame
from ..tools.vector2 import Vector2

class SysText(pygame.sprite.Sprite):
    """
    文本
    """
    def __init__(
            self, *args,
            pos: Vector2=Vector2(0, 0),
            text: str = "",
            color: pygame.Color = pygame.Color(255, 255, 255, 255),
            background: pygame.Color = None,
            name: str,
            size: int,
            bold: bool=False,
            italic: bool=False,
            antialias: bool=False, **kwargs
        ):
        self.__font = pygame.font.SysFont(name, size, bold, italic)
        self.__text = text
        self.__color = color
        self.__background = background
        self.__name = name
        self.__size = size
        self.__bold = bold
        self.__italic = italic
        self.__antialias = antialias
        self.__image = self.__font.render(self.__text, self.__antialias, color, background).convert_alpha()
        self.rect = pygame.Rect(*pos, self.__image.get_width(), self.__image.get_height())

    @property
    def font(self):
        return self.__font

    @font.setter
    def font(self, val: pygame.font.Font):
        self.__font = val
        self.__image = val.render(self.__text, self.__antialias, self.__color, self.__background).convert_alpha()
        self.rect.w = self.__image.get_width()
        self.rect.h = self.__image.get_height()

    @property
    def pos(self):
        return self.rect.topleft

    @pos.setter
    def pos(self, val: Vector2):
        self.rect.topleft = (val.x, val.y)

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, val: str):
        self.__text = val
        self.__image = self.__font.render(val, self.__antialias, self.__color, self.__background).convert_alpha()
        self.rect.w = self.__image.get_width()
        self.rect.h = self.__image.get_height()

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, val: pygame.Color):
        self.__color = val
        self.__image = self.__font.render(self.__text, self.__antialias, val, self.__background).convert_alpha()
        self.rect.w = self.__image.get_width()
        self.rect.h = self.__image.get_height()

    @property
    def background(self):
        return self.__background

    @background.setter
    def background(self, val: pygame.Color):
        self.__background = val
        self.__image = self.__font.render(self.__text, self.__antialias, self.__color, val).convert_alpha()
        self.rect.w = self.__image.get_width()
        self.rect.h = self.__image.get_height()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val: str):
        self.__name = val
        self.font = pygame.font.SysFont(val, self.__size, self.__bold, self.__italic)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val: int):
        self.__size = val
        self.font = pygame.font.SysFont(self.__name, val, self.__bold, self.__italic)

    @property
    def bold(self):
        return self.__bold
    @bold.setter
    def bold(self, val: bool):
        self.__bold = val
        self.font = pygame.font.SysFont(self.__name, self.__size, val, self.__italic)

    @property
    def italic(self):
        return self.__italic
    @italic.setter
    def italic(self, val: bool):
        self.__italic = val
        self.font = pygame.font.SysFont(self.__name, self.__size, self.__bold, val)

    @property
    def antialias(self):
        return self.__antialias

    @antialias.setter
    def antialias(self, val: bool):
        self.__antialias = val
        self.__image = self.__font.render(self.__text, val, self.__color, self.__background).convert_alpha()
        self.rect.w = self.__image.get_width()
        self.rect.h = self.__image.get_height()

    @property
    def image(self):
        return self.__image

    def draw(self, screen: pygame.Surface):
        screen.blit(self.__image, self.rect)

class FileText(pygame.sprite.Sprite):
    def __init__(self, *args,
        path: str,
        size: int | float,
        text: str = "",
        color: pygame.Color = pygame.Color(255, 255, 255),
        background: pygame.Color = None,
        antialias: bool = False,
        pos: Vector2 = Vector2(0, 0),
        **kwargs):
        self.__font = pygame.font.Font(path, size)
        self.__path = path
        self.__size = size
        self.__text = text
        self.__color = color
        self.__background = background
        self.__antialias = antialias
        self.__image = self.__font.render(text, antialias, color, background).convert_alpha()
        self.rect = pygame.Rect(*pos, self.__image.get_width(), self.__image.get_height())

    @property
    def font(self):
        return self.__font
    @font.setter
    def font(self, val: pygame.font.Font):
        self.__font = val
        self.__image = val.render(self.__text, self.__antialias, self.__color, self.__background).convert_alpha()
        self.rect.w = self.__image.get_width()
        self.rect.h = self.__image.get_height()


    @property
    def path(self):
        return self.__path
    @path.setter
    def path(self, val: str):
        self.__path = val
        self.font = pygame.font.Font(val, self.__size)

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, val: int | float):
        self.__size = val
        self.font = pygame.font.Font(self.__path, val)

    @property
    def text(self):
        return self.__text
    @text.setter
    def text(self, val: str):
        self.__text = val
        self.__image = self.__font.render(val, self.__antialias, self.__color, self.__background).convert_alpha()
        self.rect.w = self.__image.get_width()
        self.rect.h = self.__image.get_height()

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, val: pygame.Color):
        self.__color = val
        self.__image = self.__font.render(self.__text, self.__antialias, val, self.__background).convert_alpha()

    @property
    def background(self):
        return self.__background
    @background.setter
    def background(self, val: pygame.Color):
        self.__background = val
        self.__image = self.__font.render(self.__text, self.__antialias, self.__color, val).convert_alpha()

    @property
    def antialias(self):
        return self.__antialias

    @antialias.setter
    def antialias(self, val: bool):
        self.__antialias = val
        self.__image = self.__font.render(self.__text, val, self.__color, self.__background).convert_alpha()

    @property
    def pos(self):
        return self.rect.topleft
    @pos.setter
    def pos(self, val: Vector2):
        self.rect.topleft = (val.x, val.y)

    @property
    def image(self):
        return self.__image

    def draw(self, screen: pygame.Surface):
        screen.blit(self.__image, self.rect)


__all__ = ['SysText', 'FileText']