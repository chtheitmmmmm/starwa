from esign import Button, stateDefine

@stateDefine('DIS')
class DisableButton(Button):
    __slots__ = []
    def disable(self):
        self.switch('DIS')
        self.action('dis')


__all__ = ['DisableButton']