from esign import *

class AcceItem(MovableItem):
    def __init__(
        self,
        *args,
        accelerate: Vector2 | None=Vector2(0, 0),   # 当传入 None 时，表示继承者可能已经在类中编写了其实例共有的加速度
        **kwargs
    ):
        super(AcceItem, self).__init__(*args, **kwargs)
        if accelerate:
            self.accelerate = accelerate.copy()

    def update(self, *args, **kwargs) -> None:
        self.speed += self.accelerate
        return super(AcceItem, self).update(*args, **kwargs)
