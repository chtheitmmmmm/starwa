from esign import *
from mediapool import *

@stateDefine(
    'PENDDING'  ,   # 正在等待用户选择
    'SINGLE'    ,   # 用户点击了单人游戏
    'MULTI'     ,   # 用户点击了联机游戏
)
class MenuPage(metaclass=page({
        'bg'    : Item,
        'bgm'   : Audio,
        'title' : SimpleItem,
        'single': Button,
        'multi' : Button,
    })):

    def load(self):
        self.bgm.play(-1)
        midalign_verticalItem(self.app.screen, self.single)
        midalign_verticalItem(self.app.screen, self.multi)
        self.modes = ButtonGroup(self.single, self.multi)
        self.switch('PENDDING')

    def hide(self):
        self.switch('PENDDING')
        self.bgm.fadeout(1000)
        self.modes.resume()
        self.bg.action(ORD)

    def tosingle(self):
        self.switch('SINGLE')

    def tomulti(self):
        self.switch('MULTI')

    def update(self):
        self.modes.update()
        self.bg.update()
        if self.modes.state == self.modes.CLICKED:
            if self.modes.button == self.single:
                self.tosingle()
            else:
                self.tomulti()

    def handle(self, e: pygame.event.Event):
        self.modes.handle(e)

menupg = MenuPage(**{
    'single': Button(
        media = Media({
        ORD: {
            ACTIONS : [{
                AUDIO : None,
                FRAME : FrameGroup([
                    fp.bail("ui", 'button', 'sp')[0]
                ])
            }],
            ITER_TIME : 1
        },
        'touch': {
            ACTIONS: [{
                AUDIO: ap.bail('button', 'menupg')[1],
                FRAME: FrameGroup([
                    fp.bail('ui', 'button', 'sp')[1]
            ])}],
            ITER_TIME: 1
        },
        'click': {
            ACTIONS: [{
                AUDIO: ap.bail('button', 'menupg')[0],
                FRAME: FrameGroup([
                    fp.bail('ui', 'button', 'sp')[2]
                ])
            }, {
                AUDIO: None,
                FRAME: FrameGroup([
                    fp.bail('ui', 'button', 'sp')[1]
            ])}],
            ITER_TIME: 1
        }
    }, ORD),
        pos   = Vector2(0, 400)
    ),
    'multi' : Button(
        media = Media({
        ORD: {
            ACTIONS: [{
                AUDIO: None,
                FRAME: FrameGroup([
                    fp.bail("ui", 'button', 'mp')[0]
                ])
            }],
            ITER_TIME: 1
        },
        'touch': {
            ACTIONS: [{
                AUDIO: ap.bail('button', 'menupg')[1],
                FRAME: FrameGroup([
                    fp.bail('ui', 'button', 'mp')[1]
                ])
            }],
            ITER_TIME: 1
        },
        'click': {
            ACTIONS: [{
                AUDIO: ap.bail('button', 'menupg')[0],
                FRAME: FrameGroup([
                    fp.bail('ui', 'button', 'mp')[2]
                ])
            }, {
                AUDIO: None,
                FRAME: FrameGroup([
                    fp.bail('ui', 'button', 'mp')[1]
                ])
            }],
            ITER_TIME: 1
        }
    }, ORD),
        pos   = Vector2(0, 500)
    ),
    'title' : SimpleItem(
        f     = fp.bail('bg', 'title')[0],
        pos   = Vector2(0, 0)
    ),
    'bg'    : Item(
        media = Media({
        ORD: {
            ACTIONS: [{
                AUDIO: None,
                FRAME: FrameGroup(fp.bail('bg', 'menupg'))
            }],
            ITER_TIME: -1
        }
    }, ORD),
        pos   = Vector2(0, 0)
    ),
    'bgm'   : ap.bail('bg')[1]
})

__all__ = ['menupg']