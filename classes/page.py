from pygame.sprite import Sprite, Group
from pygame import Surface

# 页面类，一个基类
class Page(list[Sprite | Group]):
    def draw(self, screen: Surface):
        map(lambda drawable: drawable.draw(screen), self)

# 菜单页面类
class MenuPage(Page):
    pass

# 战斗页面类
class FightPage(Page):
    pass
