import pygame, sys, abc
from .media import AudioPool, FramePool
from .page import Page, Pages, page as P
from .tools.vector2 import Vector2

class AbstractApp(metaclass=abc.ABCMeta):
    """
    self.pages: {
        name1: page1,
        name2: page2
        ...
    }
    """
    def __init__(self,  *args, pages: Pages, **kwargs):
        self.pages = pages  # 保存页面
        self.pages.configure(self)

    def entry(self, name: str):
        self.pages.entry(name)

    def init(self, *args, **kwargs):
        """
        游戏启动初始化钩子，可重写
        """
        pass

    def add_page(self, *args, name, page, **kwargs):
        assert isinstance(name, str) and (isinstance(page, Pages) or type(type(page)) in P._meta_page), "A string name refers a page expected!"
        self.pages[name] = page
        page.app = self

    @abc.abstractmethod
    def run(self):
        pass

    def circle(self):
        """
        主循环函数钩子，用于继承
        """
        pass

    def handle(self, e: pygame.event.Event):
        """
        事件处理钩子，用于继承
        """
        pass

    def draw(self, screen):
        self.pages.draw(screen)

    def switchPage(self, name: str):
        self.pages.switch(name)

    def exit(self):
        # 退出游戏，可重写
        sys.exit(0)

__all__ = ['AbstractApp']