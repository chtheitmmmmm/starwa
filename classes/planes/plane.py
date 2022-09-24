from classes.media.frame import frame
from classes.media.audio import plane_audio
from classes.planes.parture import hp, controlcenter
from classes.planes.parture.weapon import gun, bullet
from myGametools import mySprite, mypoint

class Plane(mySprite.MySprite):
    def __init__(self,
                 name,
                 frame:frame.Frame,
                 position:mypoint.Mypoint,
                 audio:plane_audio.Plane_Audio,
                 controlcenter:controlcenter.ControlCenter,
                 weapon:gun.Gun,
                 hp: hp.HpFrameBar,
                 *relative_pos
                 ):
        self.name = name
        super().__init__(frame, position)
        self.audio = audio
        self.controlcenter = controlcenter
        self.controlcenter.configure(self)
        self.hp = hp
        self.weapon = weapon
        self.weapon.configure(self, *relative_pos)
        self.destoryed = False
        self.havedestoryed = False
    # 在Group中调用update, draw, hit
    def update(self):
        # update self.image
        super().update()
        self.hp.update()
        if not self.destoryed:
            # update self.rect
            self.controlcenter.control()
        else:
            self.havedestoryed = self.frame.sticked
    def fight(self, enemy_group):
        self.weapon.beginfire()
        self.weapon.update(enemy_group)
    def draw(self, screen):
        self.hp.draw(screen)
        screen.blit(self.image, self.rect)
        self.weapon.draw(screen)
        # 在Group中直接调用draw即可
    def hit(self, bullet):
        # 失去生命值
        if not self.destoryed and not self.hp.hpbar.hp.lose(bullet.hurt):
            self.destoryed = True
            self.frame.set_certain(0, self.DESTORY, True)
            self.audio.boomplay()


