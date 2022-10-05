from esign import *

class Msg(dict):
    def __init__(self, msg: dict):
        super(Msg, self).__init__(msg)

    def __getattribute__(self, item):
        if item == 'type':
            return self['type']
        elif item == 'value':
            return self['value']
        else:
            return super(Msg, self).__getattribute__(item)

__all__ = ['Msg']