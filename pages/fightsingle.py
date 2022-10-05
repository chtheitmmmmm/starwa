from esign import *
from mediapool import *
from src.verticalbg import *
from src.constants import constants
from src.player import *
from src.weapon import *
from src.enemy import *

@stateDefine('READY', 'GO', 'FIGHT')
class FightSinglePage(
    metaclass=page({
        'bg'        : VerticalBG,
        'bgm'       : Audio,
        'bgmreadygo': Audio,
        'ready'     : Item,
        'go'        : Item,
    })):

    def load(self):
        self.switch('READY')
        self.bgmreadygo.play()
        self.bgm.       play(loops=-1, fade_ms=int(self.bgmreadygo.get_length() * 1000))
        player_plane = self.app.selectpg.character.plane
        player_plane.pos = Vector2(0, self.app.constants['locations']['planeInitialVertical'])
        midalign_verticalItem(self.app.screen, player_plane)
        self.player             = SinglePlayer(
            plane = player_plane
        )
        self.enemy              = OfflineEnemyGroup(*enemyplanetypes)
        self.playerSingleGroup  = GroupSingle(self.player.plane)

    def draw(self, screen: Surface):
        self.bg.       draw(screen)
        self.player.   draw(screen)
        if self.state   == self.READY:
            self.ready.draw(screen)
        elif self.state == self.GO:
            self.go.   draw(screen)
        elif self.state == self.FIGHT:
            self.enemy.draw(screen)

    def update(self):
        self.bg.            update()
        self.player.        update(self.enemy)
        if self.state == self.READY:
            if self.ready.  update():
                self.switch('GO')
        elif self.state == self.GO:
            if self.go.     update():
                self.switch('FIGHT')
        elif self.state == self.FIGHT:  # 开始刷新敌人
            self.enemy.     update(self.playerSingleGroup)

fightsinglepg = FightSinglePage(**{
    'bgm'       : ap.bail('bg')[0],
    'bg'        : VerticalBG(
        media = Media({
        ORD: {
            ACTIONS: [{
                AUDIO: None,
                FRAME: FrameGroup(fp.bail('bg', 'battle'))
            }],
            ITER_TIME: 1
        }
    }, ORD),
        pos   = Vector2(0, 0),
        speed = constants['bg']['fightsinglepg']['speed']
    ),
    'bgmreadygo': ap.bail('bg')[2],
    'ready'     : Item(
        media = Media({
        ORD: {
            ACTIONS: [{
                AUDIO: None,
                FRAME: FrameGroup(fp.bail('bg', 'readygo', 'ready'))
            }],
            ITER_TIME: 1
        }
    }, ORD),
        pos   = Vector2(0, 0)
    ),
    'go'        : Item(
        media = Media({
        ORD: {
            ACTIONS: [{
                AUDIO: None,
                FRAME: FrameGroup(fp.bail('bg', 'readygo', 'go'))
            }],
            ITER_TIME: 1
        }
    }, ORD),
        pos   = Vector2(0, 0)),
})

__all__ = ['fightsinglepg']