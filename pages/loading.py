import socket, threading, json
import pygame.font
from esign import *
from mediapool import *
from src.msg import Msg

@stateDefine('CONNECTING', 'CONNECTED', 'ERROR', 'OK')
class LoadingPage(
    metaclass=page({
        'bg'     : TransformableItem,
        'ldbgm1' : Audio,
        'ldbgm2' : Audio,
        'ldbgm3' : Audio,
        'loading': Item
    })):
    """
    two state machine:
        player state: ['UNKNOEN', 'HOST', 'GUEST']
        self: ['CONNECTING', 'CONNECTED', 'ERROR', 'OK']
    """
    def load(self):
        self.switch('CONNECTING')
        self.ldbgmstate = StateMachine('BEGIN', 'LOADING', 'END', 'OVER')
        self.ldbgmstate.switch('BEGIN')
        self.ldbgm1.play()
        selfadaptleft(self.bg, self.app.screen)
        midalign_verticalItem(self.app.screen, self.bg)
        self.loading.rect.bottomright = self.app.constants['meta']['windowSize']
        self.server_address = self.app.constants['meta']['net']['server']
        self.encoding = self.app.constants['meta']['net']['encoding']
        self.typecode = platDict(self.app.constants['meta']['net']['protocol']['typecode'])
        self.playerstate = StateMachine('UNKNOWN', 'HOST', 'GUEST_NO', 'GUEST_OK')
        self.playerstate.switch('UNKNOWN')
        self.connection_info = FileText(
            path     = 'media/font/百度综艺简体.ttf',        # 如何从字体文件加载？
            size     = 20,
            pos      = Vector2(0, 700),
            color    = pygame.Color(225, 10, 10),
            antialias = True,
        )
        midalign_verticalItem(self.app.screen, self.connection_info)
        threading.Thread(target=self.__connect).start()         # 尝试连接服务器

    """
    connect -> recv -> <end>
    """
    def __connect(self):
        """
        连接服务器线程目标函数
        """
        self.switch('CONNECTING')
        self.connection_info.text = '正在连接服务器'
        midalign_verticalItem(self.app.screen, self.connection_info)
        self.socket = socket.socket(
            family = self.app.constants['meta']['net']['family'],
            type   = self.app.constants['meta']['net']['type']
        )
        self.socket.connect(self.server_address)
        self.socket.send(bytearray((self.typecode[self.app.selectpg.character.name], )))
        self.netthread = threading.Thread(target=self.__recv,)
        self.netthread.start()

    def __recv(self):
        """
        网络线程目标函数
        """
        try:
            while True:
                msg = self.socket.recv(2048)
                if msg:
                    self.msg = Msg(json.loads(msg.decode(self.encoding)))    # 获取服务器返回的数据
                    print('content: ', self.msg)
                    if self.playerstate.value == 'UNKNOWN':
                        # 获取连接信息
                        self.playerid = self.msg.value['id']
                        if self.msg.type == 'connect':
                            if self.msg.value['host']:
                                # 房主连接
                                self.playerstate.switch('HOST')
                                self.socket.send((json.dumps({
                                    'type': 'ready'
                                }) + '\n').encode(self.encoding))
                                break
                            else:
                                # 房客连接
                                self.playerstate.switch('GUEST_NO')
                        else:
                            raise ValueError('服务器出错，应该返回 connect 类型的消息！')
                    elif self.playerstate.value == 'GUEST_NO':
                        # 获取全局信息 global
                        if self.msg.type == 'global':
                            self.globalmsg = self.msg.value   # 根据 globalmsg 渲染当前布局
                            self.socket.send((json.dumps({
                                'type': 'ready'
                            }) + '\n').encode(encoding=self.encoding))
                            self.playerstate.switch("GUEST_OK")
                            break
        except OSError:
            print('连接中断')
            self.switch('ERROR')

    def draw(self, screen: pygame.Surface):
        self.bg.draw(screen)
        self.loading.draw(screen)
        self.connection_info.draw(screen)

    def update(self):
        self.bg.update()
        self.loading.update()
        if self.playerstate.value != 'HOST' and self.playerstate.value != 'GUEST_OK':
            if self.ldbgmstate.value == 'BEGIN':
                if not self.ldbgm1.get_num_channels():
                    self.ldbgmstate.switch('LOADING')
                    self.ldbgm2.play(-1)
        else:
            if self.ldbgm1.get_num_channels() or self.ldbgm2.get_num_channels():
                self.ldbgm1.stop()
                self.ldbgm2.stop()
                self.ldbgm3.play()
                self.connection_info.text = '连接成功，正在进入游戏'
                midalign_verticalItem(self.app.screen, self.connection_info)
            elif not self.ldbgm3.get_num_channels():
                self.switch('OK')           # 加载完成


loadingpg = LoadingPage(
    bg      = TransformableItem(
        media = Media({
            ORD: {
                ACTIONS: [{
                    AUDIO: None,
                    FRAME: FrameGroup(fp.bail('bg', 'loading', 'bg'))
                }],
                ITER_TIME: -1
            }
        }, ORD),
        pos  = Vector2(0, 0)
    ),
    loading = Item(
        media = Media({
            ORD: {
                ACTIONS: [{
                    AUDIO: None,
                    FRAME: FrameGroup(fp.bail('bg', 'loading', 'loading')[:-1] + fp.bail('bg', 'loading', 'loading')[-1::-1])
                }],
                ITER_TIME: -1
            }
        }, ORD),
        pos = Vector2(0, 0)
    ),
    ldbgm1 = ap.bail('bg')[4],
    ldbgm2 = ap.bail('bg')[5],
    ldbgm3 = ap.bail('bg')[6],
)

__all__ = ['loadingpg']