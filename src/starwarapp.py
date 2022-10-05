import sys

import pygame.display
from pygame.constants import *
from esign import *
from .constants import *

fps = constants['meta']['FPS']
@stateDefine(
    'MENU',             # 菜单
    'SINGLE',           # 单人游戏按钮被按下
    'MULTIPLE',            # 多人游戏按钮被按下
    "LOADING",          # 加载中
    "FIGHT_SINGLE",     # 单人战斗中
    "FIGHT_MULTIPLE"       # 多人战斗中
)
class StarwarApp(AbstractApp):
    """
    星野守望 APP
    """
    def __init__(self, *args, constants, **kwargs):
        super(StarwarApp, self).__init__(*args, **kwargs)
        meta = constants['meta']
        pygame.display.init()
        pygame.mixer.init()
        pygame.font.init()
        pygame.mixer.set_num_channels(128)
        screen = pygame.display.set_mode(meta['windowSize'])
        pygame.display.set_caption(f"{meta['caption']} {meta['version']}")
        pygame.display.set_icon(pygame.image.load(meta['icon']))
        self.constants = constants
        self.screen = screen
        self.timer = pygame.time.Clock()

    def entry(self, name: str):
        super(StarwarApp, self).entry(name)
        self.switch('MENU')

    @property
    def menupg(self):
        return self.pages['menupg']

    @property
    def selectpg(self):
        return self.pages['selectpg']

    @property
    def fightsinglepg(self):
        return self.pages['fightsinglepg']

    @property
    def fightmultiplepg(self):
        return self.pages['fightmultiplepg']

    @property
    def loadingpg(self):
        return self.pages['loadingpg']

    def run(self):
        try:
            self.switchPage('menupg')
            while True:
                self.circle()
        except Exception as e:
            print(e)
            self.exit()

    def update(self):
        self.pages.update()
        if self.state == self.MENU:
            if self.menupg.state == self.menupg.SINGLE:
                self.single()
            elif self.menupg.state == self.menupg.MULTI:
                self.multi()
        elif self.state == self.SINGLE or self.state == self.MULTIPLE:
            if self.selectpg.state == self.selectpg.SELECTED:
                if self.state == self.SINGLE:
                    self.singlefight()
                    print('单人游戏')
                else:
                    self.loading()
            elif self.selectpg.state == self.selectpg.BACK:
                self.switch('MENU')
                self.switchPage('menupg')
        elif self.state == self.LOADING:
            if self.loadingpg.state == self.loadingpg.OK:
                self.multifight()
                print('多人游戏')
            elif self.loadingpg.state == self.loadingpg.ERROR:
                self.menu()
                print('检测到网络错误，返回菜单页面')

    def exit(self):
        if self.state == self.LOADING:
            self.loadingpg.socket.close()
            self.loadingpg.netthread.join(0)
        elif self.state == self.FIGHT_MULTIPLE:
            self.fightmultiplepg.socket.close()
            self.fightmultiplepg.netthread.join(0)
        pygame.quit()
        sys.exit(0)

    def circle(self):
        for e in pygame.event.get():
            if e.type == QUIT:
                self.exit()
            else:
                self.handle(e)
        self.timer.tick(fps)
        self.draw(self.screen)
        self.update()
        pygame.display.update()

    def menu(self):
        self.switchPage('menupg')
        self.switch('MENU')

    def single(self):
        self.switchPage('selectpg')
        self.switch('SINGLE')

    def multi(self):
        self.switchPage('selectpg')
        self.switch('MULTIPLE')
        self.master = False     # 是否为房主，单人游戏情况下没有此属性

    def loading(self):
        self.switch('LOADING')
        self.switchPage('loadingpg')

    def singlefight(self):
        self.switch('FIGHT_SINGLE')
        self.switchPage('fightsinglepg')

    def multifight(self):
        self.switch('FIGHT_MULTIPLE')
        self.switchPage('fightmultiplepg')

    def handle(self, e):
        self.pages.handle(e)


