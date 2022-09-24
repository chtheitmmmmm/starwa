

class Bullet_Audio:
    def __init__(self, shootmedia, hitmedia):
        self.shootmedia = shootmedia
        self.hitmedia = hitmedia
    def hitplay(self):
        if self.hitmedia.get_num_channels() < 1:
            self.hitmedia.play()
    def shootplay(self):
        self.shootmedia.play()
    def copy(self):
        return Bullet_Audio(self.shootmedia, self.hitmedia)
