import pygame
from random import choice

class EnemyGroup(pygame.sprite.Group):
    def __init__(self, *planes,internal):
        super().__init__()
        self.planes = planes # 所有飞机种类
        self.lastime = pygame.time.get_ticks()
        self.internal = internal
    def update(self, enemy_group):
        for i in self.sprites():
            i.update()
            i.fight(enemy_group)
            if i.havedestoryed and not i.weapon.sprites():
                self.remove(i)
        now = pygame.time.get_ticks()
        if now - self.lastime >= self.internal:
            self.lastime = now
            self.add(choice(self.planes).copy(True))
    def draw(self, screen):
        for i in self.sprites():
            i.draw(screen)

