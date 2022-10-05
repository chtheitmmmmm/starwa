import pygame
from .constants import *
from .tools import *
from .item import *
from .media import *


# 按钮类是四状态机
@stateDefine('ORD', 'ON', 'CLICKING', 'CLICKED')
class Button(Item):
    """
    actionChain: {
        ORD: [{
            audio: none
            frame: ord
        }],
        'touch': [{
            audio: touchAudio
            frame: touchFrame
        }],
        'click': [{
            audio: clickAudio
            frame: clickFrame1
        }, {
            audio: None,
            frame: touchFrame
        }]
    }
    """
    __slots__ = []
    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)
        self.switch('ORD')

    def update(self, *args, **kwargs) -> bool:

        if self.state == self.CLICKING:
            if super(Button, self).update(*args, **kwargs):
                self.switch('CLICKED')
        elif self.state != self.CLICKED:
            super(Button, self).update()

    def click(self):
        self.action('click')
        self.switch('CLICKING')

    def touch(self):
        self.action('touch')
        self.switch('ON')

    def ord(self):
        self.action('ord')
        self.switch('ORD')

    def handle(self, e: pygame.event.Event):
        if self.state == self.ORD or self.state == self.ON:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == pygame.BUTTON_LEFT:
                if pygame.Rect.collidepoint(self.rect, e.pos):
                    self.click()
            elif e.type == pygame.MOUSEMOTION:
                if pygame.Rect.collidepoint(self.rect, e.pos):
                    if self.state != self.ON:
                        self.touch()
                else:
                    if self.state != self.ORD:
                        self.ord()

@stateDefine("ORD", "CLICKING", "CLICKED")
class ButtonGroup(pygame.sprite.Group):
    """
    管理一个按钮群，确保一个按钮在播放点击动画时其他按钮不能被按下
    """
    __slots__ = ['button']
    def __init__(self, *buttons):
        assert all(map(lambda b: isinstance(b, Button), buttons)), "Expected buttons!"
        super().__init__(buttons)
        self.button = None
        self.switch('ORD')


    def update(self):
        if self.state == self.ORD:
            for b in self.sprites():
                if b.state == b.CLICKING:
                    self.switch('CLICKING')
                    self.button = b
                else:
                    b.update()
        elif self.state == self.CLICKING:
            self.button.update()
            if self.button.state == self.button.CLICKED:
                self.switch('CLICKED')

    def resume(self):
        if self.button:
            self.button.ord()
            self.button = None
        self.switch('ORD')

    def handle(self, e: pygame.event.Event):
        if self.state == self.ORD:
            for b in self.sprites():
                b.handle(e)

__all__ = ['ButtonGroup', 'Button']
