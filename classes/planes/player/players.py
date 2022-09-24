import pygame

class Players(pygame.sprite.Group):
    def update(self, enemy_group) -> None:
        for player in self.sprites():
            player.update()
            player.fight(enemy_group)
            if player.havedestoryed:
                self.remove(player)
    def draw(self, screen):
        self.draw(screen)