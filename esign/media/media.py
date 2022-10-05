import pygame.mixer
import copy
from .audio import AudioPool
from pygame.mixer import Sound
from .frame import *
from .audio import Audio
from .frame import FrameGroup
from ..constants import *

class Media(dict):
    """
    传给Item的媒体类
    """
    __slots__ = ['actionChainName', 'actionIndex', 'iter', 'entry']
    def __init__(self, actionChains: dict, entry: str):
        """
        :param actionChains: 一个字典，用来表示动作名和动作链之间的映射关系
        :param entry: 入口动作名称
        actionChains: {
            name1: {
                actions: [{
                    audio: None             # no audio played
                    frame: frame1
                }, {
                    audio: audio2
                    frame: frame2
                }]
                itertime: -1                # negative refers to infinity play
            },
            name2: {
                actions: [{
                    audio: audio1
                    frame: frame1
                }]
                itertime: 3                 # iterate 3 times
            }
        }
        self.actionChainName    = name1
        self.actionIndex        = 0
        self.actionIndex             = self[self.actionChainName][ACTIONS][self.actionIndex]
        self.iter               = 0
        """
        for acv in actionChains.values():
            [fg[FRAME].resume() for fg in acv[ACTIONS]]     # 恢复所有已经
        super(Media, self).__init__(actionChains)
        self[entry]                     # entry exists?
        self.actionIndex = 0                 # 当前动作在动作链中的下标
        self.actionChainName = entry        # 当前动作链名称
        self.iter = 1                   # 动作链已经迭代的次数，-1代表没有执行动作链
        self.entry = entry

    def resumeCurrentAction(self):
        self.action[FRAME].resume()

    def registerActionChain(self, name: str, *actions: list[str], itertime: int):
        """
        注册动作链
        """
        self.actionChains[name] = {
            ACTIONS: actions,
            ITER_TIME: itertime
        }

    def switchActionChain(self, name: str):
        """
        设置当前动作链
        """
        self[name]  # entry exists?
        self.resumeCurrentAction()
        self.actionIndex = 0  # 当前动作在动作链中的下标
        self.actionChainName = name  # 当前动作链名称
        self.iter = 1  # 当前在动作链的第几次迭代，-1代表没有执行动作链
        if self.action[AUDIO]:
            self.action[AUDIO].play()

    def physicalLastAction(self):
        """
        返回当前动作是否为动作链中物理上的（不一定是逻辑上）最后一个动作
        """
        return self.actionIndex >= len(self[self.actionChainName][ACTIONS]) - 1

    def nextAction(self):
        """
        进入当前动作链的下一个动作
        """
        if self.physicalLastAction():
            if 0 < self.itertime <= self.iter:
                return True  # 切换下一个动作失败
            else:
                self.resumeCurrentAction()  # 将当前动作的消费清除
                self.iter += 1
        else:
            self.resumeCurrentAction()  # 将当前动作的消费清除
            self.actionIndex += 1
        if self.action[AUDIO]:
            self.action[AUDIO].play()

        return False

    @property
    def action(self):
        return self[self.actionChainName][ACTIONS][self.actionIndex]

    @property
    def image(self) -> pygame.Surface:
        return self.action[FRAME].getCurrentFrameSingle().image

    @property
    def itertime(self) -> int:
        return self[self.actionChainName][ITER_TIME]

    @property
    def audio(self) -> pygame.mixer.Sound:
        return self.action.audio

    def update(self):
        """
        返回当前动作链是否消耗殆尽，若消耗殆尽将卡在最后一帧
        """
        if self.action[FRAME].go():
            return self.nextAction()

    def copy(self):
        return Media(copy.deepcopy(self), self.entry)

__all__ = ['Media']
