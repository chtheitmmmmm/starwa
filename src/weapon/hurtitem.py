from esign import *

@stateDefine(
    'PLAIN',        # 没有输出能力
    'HITTABLE',     # 有输出能力
    'DELETABLE'     # 可以从武器中删除
)
class HurtItem(Item):
    """
    有伤害的对象，可以对目标输出伤害，但没有指定造成伤害的判定条件
    默认的update实现：
        当状态为 HITTABLE，则判断是否能score敌人，若能就hit敌人
    """
    def __init__(self, *args, hurt, **kwargs):
        super(HurtItem, self).__init__(*args, **kwargs)
        self.__hurt = hurt
        self.switch('PLAIN')

    def hit(self, aim: HpItem):
        """
        伤害一个有hp的对象
        """
        aim.lose(self.hurt)

    def score(self, aim: HpItem) -> bool:
        return False

    def update(self, *, aim_group: pygame.sprite.AbstractGroup) -> bool:
        if self.state == self.HITTABLE:
            for aim in aim_group.sprites():
                if self.score(aim):
                    self.hit(aim)
        return super(HurtItem, self).update()

    @property
    def hurt(self):
        return self.__hurt

__all__ = ['HurtItem']