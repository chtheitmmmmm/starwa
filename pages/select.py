from esign import *
from mediapool import *
from src.character import *
from src.disableButton import *
from src.plane import *
from src.hp import *
from src.verticalbg import *
from src.constants import *
from src.player import *

@stateDefine(
    'BACK'      ,   # 返回上一级页面
    'SELECTING' ,   # 正在选择
    'SELECTED'  ,   # 选择完毕
)
class SelectPage(
    metaclass=page({
        'bg'        : SimpleItem,
        'bgm'       : Audio,
        'nameframe' : SimpleItem,
        'characters': CharcterGroup,
        'larw'      : DisableButton,
        'rarw'      : DisableButton,
        'bottom'    : SimpleItem,
        'back'      : Button,
        'fight'     : Button
    })):

    def load(self):
        self.bgm.play(-1)
        self.switch('SELECTING')
        self.bottom.pos = Vector2(0, self.app.screen.get_height() - self.bottom.rect.height)
        midalign_vertical(self.bg,   self.nameframe, STICKS1)
        self.lrbt = ButtonGroup(self.larw, self.rarw)
        arwpos = constants['locations']['arw']
        self.larw.pos = arwpos
        self.rarw.pos = Vector2(self.app.screen.get_width() - arwpos.x, arwpos.y)
        midalign_horizental(self.nameframe, self.larw, STICKS2)
        for character in self.characters:
            character.plane.pos = Vector2(0, 300)
            midalign_vertical(self.bg, character.plane, STICKS1)
            midalign(character.nameitem, self.nameframe, STICKS2)
            character.people.rect.bottomright = self.app.screen.get_size()
        self.characters.switchCharacter(0)
        self.fight.rect.topright = (self.app.screen.get_width(), self.back.pos.y)
        self.fb = ButtonGroup(self.fight, self.back)

    def update(self):
        if self.characters.crt <= 0:
            if self.larw.state != self.larw.DIS:
                self.larw.disable()
        else:
            if self.larw.state == self.larw.DIS:
                self.larw.ord()
        if self.characters.crt >= len(self.characters) - 1:
            if self.rarw.state != self.larw.DIS:
                self.rarw.disable()
        else:
            if self.rarw.state == self.larw.DIS:
                self.rarw.ord()
        if self.lrbt.state == self.lrbt.CLICKED:
            if self.lrbt.button == self.larw:
                self.characters.switchLastCharacter()
                midalign(self.character.nameitem, self.nameframe, STICKS2)
                self.character.people.rect.bottomright = self.app.screen.get_size()
            else:
                self.characters.switchNextCharacter()
                midalign(self.character.nameitem, self.nameframe, STICKS2)
                self.character.people.rect.bottomright = self.app.screen.get_size()
            self.lrbt.resume()
        if self.fb.state == self.fb.CLICKED:
            if self.fb.button == self.back:
                self.switch('BACK')
            else:
                self.switch('SELECTED')
        else:
            self.lrbt.update()
        self.character.update()
        self.fb.update()

    def draw(self, screen):
        self.bg.draw(screen)
        self.nameframe.draw(screen)
        self.bottom.draw(screen)
        self.lrbt.draw(screen)
        self.characters.draw(screen)
        self.fb.draw(screen)

    def handle(self, e: pygame.event.Event):
        self.lrbt.handle(e)
        self.fb.handle(e)

    def hide(self):
        self.bgm.fadeout(1000)
        if self.state == self.BACK:
            self.fb.resume()
        else:
            self.lrbt.resume()
        self.switch('SELECTING')

    @property
    def character(self):
        """
        获取当前选中的角色
        """
        return self.characters.character


selectpg = SelectPage(
    bg          = SimpleItem(
        f   = fp.bail('bg', 'select')[0],
        pos = Vector2(0, 0)
    ),
    bgm         = ap.bail('bg')[3],
    nameframe   = SimpleItem(
        f   = fp.bail('bg', 'nameframe')[0],
        pos = Vector2(0, 100)
    ),
    characters  = CharcterGroup([
        Character(
            'lion',
            Item(
                media = Media({
                ORD: {
                    ACTIONS: [{
                        AUDIO: None,
                        FRAME: FrameGroup(fp.bail('plane', 'apperance', 'player', 'lion', 'nameitem'))
                    }],
                    ITER_TIME: 1
                }
            }, ORD),
                pos   = Vector2(0, 0)
            ),
            Item(
                media = Media({
                ORD: {
                    ACTIONS: [{
                        AUDIO: None,
                        FRAME: FrameGroup(fp.bail('plane', 'apperance', 'player', 'lion', 'people'))
                    }],
                    ITER_TIME: 1
                }
            }, ORD),
                pos   = Vector2(0, 0)
            ),
            ap.bail('plane', 'sentence', 'player', 'lion'),
            LionPlane(
                hppos = Vector2(10, 10)
            )
        ),
        Character(
            'bird',
            Item(
                media = Media({
                ORD: {
                    ACTIONS: [{
                        AUDIO: None,
                        FRAME: FrameGroup(fp.bail('plane', 'apperance', 'player', 'bird', 'nameitem'))
                    }],
                    ITER_TIME: 1
                }
            }, ORD),
                pos   = Vector2(0, 0)
            ),
            Item(
                media = Media({
                ORD: {
                    ACTIONS: [{
                        AUDIO: None,
                        FRAME: FrameGroup(fp.bail('plane', 'apperance', 'player', 'bird', 'people'))
                    }],
                    ITER_TIME: 1
                }
            }, ORD),
                pos   = Vector2(0, 0)
            ),
            ap.bail('plane', 'sentence', 'player', 'bird'),
            BirdPlane(
                hppos = Vector2(10, 10)
            )
        )
    ]),
    larw        = DisableButton(
        media = Media({
        ORD: {
            ACTIONS: [{
                AUDIO: None,
                FRAME: FrameGroup([fp.bail('ui', 'button', 'lplane')[1]])
            }],
            ITER_TIME: 1
        },
        'touch': {
            ACTIONS: [{
                AUDIO: None,
                FRAME: FrameGroup([fp.bail('ui', 'button', 'lplane')[2]])
            }],
            ITER_TIME: 1
        },
        'click': {
            ACTIONS: [{
                AUDIO: ap.bail('button', 'arw')[0],
                FRAME: FrameGroup([fp.bail('ui', 'button', 'lplane')[2]])
            }],
            ITER_TIME: 1
        },
        "dis": {
            ACTIONS: [{
                AUDIO: None,
                FRAME: FrameGroup([fp.bail('ui', 'button', 'lplane')[0]])
            }],
            ITER_TIME: 1
        }
    }, "ord"),
        pos   = Vector2(0, 0)
    ),
    rarw        = DisableButton(
        media = Media({
        ORD: {
            ACTIONS: [{
                AUDIO: None,
                FRAME: FrameGroup([fp.bail('ui', 'button', 'nplane')[1]])
            }],
            ITER_TIME: 1
        },
        'touch': {
            ACTIONS: [{
                AUDIO: None,
                FRAME: FrameGroup([fp.bail('ui', 'button', 'nplane')[2]])
            }],
            ITER_TIME: 1
        },
        'click': {
            ACTIONS: [{
                AUDIO: ap.bail('button', 'arw')[0],
                FRAME: FrameGroup([fp.bail('ui', 'button', 'nplane')[2]])
            }],
            ITER_TIME: 1
        },
        "dis": {
            ACTIONS: [{
                AUDIO: None,
                FRAME: FrameGroup([fp.bail('ui', 'button', 'nplane')[0]])
            }],
            ITER_TIME: 1
        }
    }, "ord"),
        pos   = Vector2(0, 0)
    ),
    bottom      = SimpleItem(
        f   = fp.bail('bg', 'bottom')[0],
        pos = Vector2(0, 0)
    ),
    back        = Button(
        media = Media({
        ORD: {
            ACTIONS: [{
                AUDIO: None,
                FRAME: FrameGroup([fp.bail('ui', 'button', 'back')[0]])
            }],
            ITER_TIME: 1
        },
        'touch': {
            ACTIONS: [{
                AUDIO: ap.bail('button', 'menupg')[1],
                FRAME: FrameGroup([fp.bail('ui', 'button', 'back')[1]])
            }],
            ITER_TIME: 1
        },
        'click': {
            ACTIONS: [{
                AUDIO: ap.bail('button', 'back')[0],
                FRAME: FrameGroup([fp.bail('ui', 'button', 'back')[2]])
            }, {
                AUDIO: None,
                FRAME: FrameGroup([fp.bail('ui', 'button', 'back')[1]])
            }],
            ITER_TIME: 1
        }
    }, ORD),
        pos   = Vector2(0, 20)
    ),
    fight       = Button(
        media = Media({
        ORD: {
            ACTIONS: [{
                AUDIO: None,
                FRAME: FrameGroup([fp.bail('ui', 'button', 'fight')[0]])
            }],
            ITER_TIME: 1
        },
        'touch': {
            ACTIONS: [{
                AUDIO: ap.bail('button', 'menupg')[1],
                FRAME: FrameGroup([fp.bail('ui', 'button', 'fight')[1]])
            }],
            ITER_TIME: 1
        },
        'click': {
            ACTIONS: [{
                AUDIO: ap.bail('button', 'fight')[0],
                FRAME: FrameGroup([fp.bail('ui', 'button', 'fight')[2]])
            }, {
                AUDIO: None,
                FRAME: FrameGroup([fp.bail('ui', 'button', 'fight')[1]])
            }],
            ITER_TIME: 1
        }
    }, ORD),
        pos   = Vector2(0, 20)
    ),
)

__all__ = ['selectpg']