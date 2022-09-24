import pygame
from . import bullet
from myGametools import mypoint
from init import constants


class Gun(pygame.sprite.Group):
    '''
    gun weapon, constantly product, update and draw them
    remenber to configure
    '''
    def __init__(self,
                 interval,
                 bullet):
        super().__init__()
        self.interval = interval
        self.bullet = bullet
        self.beginfired = False
    def beginfire(self):
        if not self.beginfired:
            self.lasttime = pygame.time.get_ticks()
            self.beginfired = True
    def configure(self, plane, *relative_pos):
        self.plane = plane
        self.relative_pos = relative_pos
        self.update(None)
    def update(self, anemy_group:pygame.sprite.Group | None):
        if self.beginfired:
            now = pygame.time.get_ticks()
            if now - self.lasttime >= self.interval:
                b = self.bullet
                r = self.plane.rect
                self.lasttime = now
                addone = None
                for i in self.relative_pos:
                    addone = bullet.Bullet(b.hurt,
                                        b.frame.copy(),
                                        b.audio,
                                        # 中心和战斗机对齐，位置由relative_pos决定
                                        mypoint.Mypoint((r.left + r.width * i, r.centery-b.rect.height//2)),
                                        b.speed[:],
                                        b.accelerate[:],
                                        b.LEISURE)
                    self.add(addone)
                addone.audio.shootplay()
            for i in self.sprites():
                i.update()
                if not i.boomed:
                    i.collide_update(anemy_group)
                    if i.rect.bottom < 0:
                        self.remove(i)
                elif i.haveboomed:
                    self.remove(i)

    def copy(self):
        return Gun(self.interval, self.bullet)



class Enemy_Gun(Gun):
    def update(self, anemy_group: pygame.sprite.Group):
        if self.beginfired:
            now = pygame.time.get_ticks()
            if now - self.lasttime >= self.interval:
                b = self.bullet
                r = self.plane.rect
                self.lasttime = now
                addone = None
                for i in self.relative_pos:
                    addone = bullet.Bullet(b.hurt,
                                           b.frame.copy(),
                                           b.audio,
                                           # 中心和战斗机对齐，位置由relative_pos决定
                                           mypoint.Mypoint((r.left + r.width * i, r.centery - b.rect.height // 2)),
                                           b.speed[:],
                                           b.accelerate[:],
                                           b.LEISURE)
                    self.add(addone)
                addone.audio.shootplay()
            for i in self.sprites():
                i.update()
                if not i.boomed:
                    i.collide_update(anemy_group)
                elif i.haveboomed or i.rect.bottom > 0:
                    self.remove(i)
    def copy(self):
        return Enemy_Gun(self.interval, self.bullet)

class Sa_1_Gun(Enemy_Gun):
    def update(self, anemy_group:pygame.sprite.Group):
        if self.beginfired:
            now = pygame.time.get_ticks()
            if now - self.lasttime >= self.interval:
                b = self.bullet
                r = self.plane.rect
                self.lasttime = now
                addone = None
                if self.plane.controlcenter.engine.acceing and not self.plane.destoryed:
                    for i in self.relative_pos:
                        addone = bullet.Bullet(b.hurt,
                                            b.frame.copy(),
                                            b.audio,
                                            # 中心和战斗机对齐，位置由relative_pos决定
                                            mypoint.Mypoint((r.left + r.width * i, r.centery-b.rect.height//2)),
                                            b.speed[:],
                                            b.accelerate[:],
                                            b.LEISURE)
                        self.add(addone)
                    addone.audio.shootplay()
            for i in self.sprites():
                i.update()
                if not i.boomed:
                    i.collide_update(anemy_group)
                    if i.rect.top > constants.SCREEN_SIZE[1]:
                        self.remove(i)
                elif i.haveboomed :
                    self.remove(i)

    def copy(self):
        return Sa_1_Gun(self.interval, self.bullet)




