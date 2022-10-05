from .media import *
from .audio import *
from .frame import *
from .text  import *

"""
本包定义媒体池 MediaPool 和复用媒体对象 Media
最终落实到每一个Item应该都配备一个Media。

一个Media由动作链ActionChain组成
每一个ActionChain又由动作Action组成。
每一个Action又由Audio和FrameGroup组成
当一个Item执行某一个ActionChain时，每个Action的Audio和Frame均依次开始工作。
"""