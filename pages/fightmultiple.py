import socket
import threading, json
from esign import *
from mediapool import *
from src.verticalbg import *
from src.player import *
from src.msg import Msg
from src.enemy import *

class FightMultiplePage(metaclass=page({})):
    def load(self):
        self.bgm = self.app.fightsinglepg.bgm
        self.socket = self.app.loadingpg.socket
        self.netthread = threading.Thread(target=self.recv,)
        self.encoding = self.app.loadingpg.encoding
        self.typecode = self.app.loadingpg.typecode
        self.bgm.play(-1)
        if self.app.loadingpg.playerstate.value == 'HOST':
            self.__host_join()
        elif self.app.loadingpg.playerstate.value == 'GUEST_OK':
            self.__guest_join()
        else:
            raise ValueError('Cannot understand the state!')
        self.netthread.start()      # 开启网络线程

    def __host_join(self):
        """
        以房主身份加入
        """
        self.bg = self.app.fightsinglepg.bg.copy()
        self.bg.pos = Vector2(0, 0)
        self.playergroup = PlayerGroup(
            main_player = OnlinePlayer(
                plane = self.app.selectpg.character.plane,
                id    = self.app.loadingpg.playerid
            )
        )
        self.enemygroup = OnlineEnemyGroup(*enemyplanetypes)
        self.enemygroup.switch('HOST')

    def __guest_join(self):
        """
        以宾客身份加入
        """
        self.bg = self.app.fightsinglepg.bg.copy()
        self.bg.pos = Vector2(*self.app.loadingpg.globalmsg['bgpos'])
        self.playergroup = PlayerGroup(
            main_player=OnlinePlayer(
                plane=self.app.selectpg.character.plane,
                id=self.app.loadingpg.playerid
            )
        )
        self.playergroup.init(self.app.loadingpg.globalmsg)
        self.enemygroup = OnlineEnemyGroup(*enemyplanetypes)
        self.enemygroup.switch("GUEST")
        self.enemygroup.init(self.app.loadingpg.globalmsg)

    def recv(self):
        """
        套接字开始工作
        """
        try:
            while True:
                data = self.socket.recv(1048576)
                if data:
                    contents = data.decode(self.encoding).split('\n')
                    for content in contents:
                        if not content:
                            continue
                        content = json.loads(content)
                        print('content: ', content)
                        msg = Msg(content)
                        if msg.type == 'host':
                            self.switchHost()
                        elif msg.type == 'enemy_instructor':
                            self.enemygroup.process(msg.value)
                        elif msg.type == 'require_global':
                            self.socket.send(self.globalData())
                        else:
                            self.playergroup.process(msg)
        except OSError:
            print('断开连接')

    def globalData(self):
        """
        生成全局数据
        """
        return (json.dumps({
            'type': 'global',
            'value': {
                'players': [{
                    'id': player.id,
                    'code': player.plane.code,
                    'speed': [*player.plane.speed],
                    'accelerate': [*player.plane.accelerate],
                    'pos': [*player.plane.pos],
                    'hp': player.plane.hp.left
                } for player in self.playergroup.players],
                'enemys': [{
                    'id': enemy.id,
                    'code': enemy.plane.code,
                    'pos': [*enemy.plane.pos],
                    'hp': enemy.plane.hp.left
                } for enemy in self.enemygroup.enemys],
                'bgpos': [*self.bg.pos]
            }
        }) + '\n').encode(self.encoding)

    def switchHost(self):
        self.enemygroup.switch('HOST')

    def draw(self, screen: pygame.Surface):
        self.bg.draw(screen)
        self.enemygroup.draw(screen)
        self.playergroup.draw(screen)

    def update(self):
        self.bg.update()
        instructors = self.playergroup.update(self.enemygroup)
        for instructor in instructors:
            self.socket.send((json.dumps(instructor) + '\n').encode(self.encoding))
        if self.enemygroup.state == self.enemygroup.HOST:
            instructors = self.enemygroup.update(self.playergroup)
            for instructor in instructors:
                self.socket.send((json.dumps(instructor) + '\n').encode(self.encoding))
        else:
            self.enemygroup.update(self.playergroup)
fightmultiplepg = FightMultiplePage()

__all__ = ['FightMultiplePage', 'fightmultiplepg']