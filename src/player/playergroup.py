import pygame
from esign import *
from .player import *
from .playerplane import *

class PlayerGroup(pygame.sprite.Group):
    def __init__(self, main_player: OnlinePlayer):
        super(PlayerGroup, self).__init__(main_player.plane)
        self.players = [main_player]

    def getPlayerById(self, id: str):
        for player in self.players:
            if player.id == id:
                return player
        return None

    def getPlaneByCode(self, code: int):
        if code == 1:
            return LionPlane
        elif code == 2:
            return BirdPlane

    def init(self, globalmsg: dict):
        """
        根据全局信息初始化
        """
        for player in globalmsg['players']:
            newplayer = OnlinePlayer(
                id = player['id'],
                plane = self.getPlaneByCode(player['code'])(
                    hprelative = True,
                    hppos = Vector2(0, 128)
                ),
            )
            newplayer.plane.lose(newplayer.plane.hp.total - player['hp'])
            newplayer.plane.pos = Vector2(*player['pos'])
            newplayer.plane.speed = Vector2(*player['speed'])
            newplayer.plane.accelerate = Vector2(*player['accelerate'])
            newplayer.switch('PLAIN')
            self.players.append(newplayer)
            self.add(newplayer.plane)

    def join(self, info: dict):
        """
        添加玩家
        {
            type: 'player_join'
            value: {
                id: ...
                code: ...
            }
        }
        """
        planetype = self.getPlaneByCode(info['code'])
        newplayer = OnlinePlayer(plane = planetype(hprelative=True, hppos=Vector2(0, 128)), id = info['id'])
        self.players.append(newplayer)
        self.add(newplayer.plane)

    def instructor(self, info: dict):
        insplayer = self.getPlayerById(info['id'])
        if insplayer:
            insplayer.process(info)
        else:
            raise ValueError('Cannot find such player!')

    def leave(self, info: dict):
        """
        当接收到玩家离开的消息
        """
        leaveplayer = self.getPlayerById(info['id'])
        if leaveplayer:
            self.players.remove(leaveplayer)
            leaveplayer.plane.kill()
        else:
            raise ValueError('Cannot find such player!')

    def update(self, enemy_group) -> list[dict]:
        """
        返回玩家指令
        """
        for player in self.players:
            if player == self.players[0]:
                keys = pygame.key.get_pressed()
                player.w = keys[pygame.K_w]
                player.a = keys[pygame.K_a]
                player.s = keys[pygame.K_s]
                player.d = keys[pygame.K_d]
                player.space = keys[pygame.K_SPACE]
            player.update(enemy_group)
        if self.players:
            insturctors = self.players[0].instructors[:]
            self.players[0].instructors.clear()
            return insturctors
        else:
            return []

    def vincible(self, info: dict):
        vincibleplayer = self.getPlayerById(info['id'])
        if vincibleplayer:
            vincibleplayer.switch('PLAIN')
        else:
            raise ValueError('Cannot find such player!')

    def process(self, info):
        if info.type == 'player_instructor':
            self.instructor(info.value)
        elif info.type == 'player_leave':
            self.leave(info.value)
        elif info.type == 'player_join':
            self.join(info.value)
        elif info.type == 'player_vincible':
            self.vincible(info.value)

    def draw(self, screen: pygame.Surface):
        for plane in self.sprites():
            plane.draw(screen)


__all__ = ['PlayerGroup']
