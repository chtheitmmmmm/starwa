class Plane_Audio:
    def __init__(self, boom_audio):
        self.boom_audio = boom_audio

    def boomplay(self):
        self.boom_audio.play()

