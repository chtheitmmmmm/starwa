class Button_Audio:
    def __init__(self, button_on_audio, button_down_audio):
        self.button_down_audio = button_down_audio
        self.button_on_audio   = button_on_audio

    def downplay(self):
        self.button_down_audio.play()

    def onplay(self):
        self.button_on_audio.play()

