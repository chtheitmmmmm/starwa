import pygame
class Audio(pygame.mixer.Sound):
    def __deepcopy__(self, memodict={}):
        return self

class AudioPool(dict):
    """
    帧池，用于管理所有复用音频
    """
    def __init__(self, audioRoot:str):
        """
        :param audioRoot: 根目录，将会在此目录下工作
        """
        self.root = audioRoot

    def registers(self, finders: list[dict]):
        """
        nameitem: {
            name1: [
                filename1,
                filename2,
                filename3
            ],
            name2: {
                name21: [
                    filename1
                ]
                name22: [
                    filename1,
                    filename2
                ]
            }
        }
        """
        path = self
        queue = [(path, finders)]        # 广搜队列
        while queue:
            p, v = queue.pop(0)
            for n in v:
                if isinstance(v[n], list):
                    audioList = []
                    for audio in v[n]:
                        audioList.append(Audio(f"{self.root}/{audio}"))
                    p[n] = audioList
                elif isinstance(v[n], dict):
                    queue.append((p.setdefault(n, v[n]),v[n]))
                else:
                    raise TypeError("dict or list is only expected.")

    def bail(self, *wraperPath): # 从水池中舀水，返回dict或FrameNum或自身或直接报错
        if len(wraperPath):
            assert all([isinstance(item, str) for item in wraperPath])
            r = self
            for i in wraperPath:
                r = r[i]
            return r
        else:
            return self

__all__ = ['Audio', 'AudioPool']