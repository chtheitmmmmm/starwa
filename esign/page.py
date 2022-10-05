import pygame.event
from pygame.sprite import Sprite, AbstractGroup, GroupSingle
from pygame import Surface
from .media import Audio
from .item import Item
from .tools import *
"""
页面元类，方便地生成独特的页面类。有利于代码阅读和 debug
缺点：所有属性都必须在items中以字典形式给出，一个不能多一个不能少
注意：如果继承，且不调用super，则只需要
"""

def page(items: dict):
    class _Page(type):
        def __new__(cls, name, fathers, namespace):
            nonlocal items
            page._meta_page.add(cls)
            def __init__(self, **kwargs):
                nonlocal items
                if set(items) != set(kwargs):
                    raise ValueError(f'Not equal to signal: {tuple(items)}')
                for key, value in items.items():
                    attr = kwargs[key]
                    if not isinstance(attr, value):
                        raise TypeError('Component parsed error!')
                    setattr(self, key, attr)

            def draw(self, screen: Surface):
                nonlocal items
                for key in items:
                    i = getattr(self, key)
                    if isinstance(i, Item | AbstractGroup):
                        i.draw(screen)

            def update(self):
                nonlocal items
                [getattr(self, key).update() if isinstance(key, Item | AbstractGroup) else "" for key in items]

            def handle(self, e: pygame.event.Event):
                pass

            def hide(self):
                pass

            def load(self):
                pass

            if namespace.get('__slots__'):
                namespace['__slots__'] = list(set(namespace['__slots__']).union(set(items)))
            namespace['__init__'] = __init__
            namespace.setdefault('draw', draw)
            namespace.setdefault('update', update)
            namespace.setdefault('handle', handle)
            namespace.setdefault('hide', hide)
            namespace.setdefault('load', load)
            return super().__new__(cls, name, fathers, namespace)
    return _Page

page._meta_page = set()
"""
页面类，可以继承。
缺点：代码弹性太大，不好控制组件属性
"""
class Page(dict):
    """
    items: {
        name1: item1,
        name2: item2,
    }
    """
    def __init__(self, items:dict):
        super(Page, self).__init__(items)

    def draw(self, screen: Surface):
        [g.draw(screen) if isinstance(g, Item | AbstractGroup) else "" for g in self.values()]

    def update(self):
        [g.update() if isinstance(g, Item | AbstractGroup) else "" for g in self.values()]

    def handle(self, e: pygame.event.Event):
        """
        时间处理钩子
        """
        pass

    def hide(self):
        """
        当页面被切换走调用的函数，一个钩子，被pages调用
        """
        pass

    def load(self):
        """
        当页面设为当前页面调用的函数
        """
        pass

class Pages(dict):
    """
    集中管理所有页面，提供给app类相关接口。
    """
    def __init__(self, pages: dict={}):
        for n, p in pages.items():
            assert isinstance(n, str) and (isinstance(p, Page) or (type(type(p)) in page._meta_page)), TypeError('Error')
        super(Pages, self).__init__(pages)

    def entry(self, name: str):
        """
        选择入口页面
        """
        self.current = name
        self.currentPage.load()

    def configure(self, app: AbstractGroup):
        self.__app = app
        for n, p in self.items():
            p.app = app

    @property
    def app(self):
        return self.__app

    @property
    def currentPage(self) -> Page:
        return self[self.current]

    def update(self):
        self.currentPage.update()

    def switch(self, name: str):
        self.currentPage.hide()
        self.current = name
        self.currentPage.load()

    def draw(self, screen: Surface):
        self.currentPage.draw(screen)

    def handle(self, e: pygame.event.Event):
        self.currentPage.handle(e)