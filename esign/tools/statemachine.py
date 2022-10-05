"""
所有工具不会自动分配默认状态，需要用户自己分配默认状态
对于任意情况，最好的解决方案还是装饰器
"""

def _illegal_(states):
    assert len(set(states)) == len(states), "Repeat state detected."
    for state in states:
        if state == 'switch':
            raise ValueError('"switch" is protected for function switch(self).')
        elif state == 'state':
            raise ValueError('"state" is protected for attribute state.')
        elif state == 'states':
            raise ValueError('"states" is protected for readonly attribute states.')
        if not isinstance(state, str):
            raise TypeError("Non string state detected!")
        if not state.isidentifier():
            raise ValueError("An identifier state value is expected.")
        if not state.isupper():
            Warning('Uppercase is suggested as state value.')
    return True


"""
类对象解决方案
"""
class StateMachine:
    """
    考虑到app和button等很多对象有状态的概念，故定义此状态机类
    状态机在创建之后就不可改变，只能通过switch切换
    """
    __slots__ = ['__states', '__value']
    def __init__(self, *states):
        """
        :param states: 状态列表，值只能是字符串
        :param current: 初始状态，值可以为下标也可以为字符串，但均需要能够在states中找到
        """
        _illegal_(states)
        self.__states = states

    @property
    def states(self):
        return self.__states

    @property
    def value(self):
        return self.__value

    def switch(self, name: str | int):
        """
        切换到新状态
        """
        if isinstance(name, str):
            self.__states.index(name)
            self.__value = name
        elif isinstance(name, int):
            self.__value = self.__states[name]
        else:
            raise TypeError("Str or int is expected.")

    def __setattr__(self, key, value):

        if key != '_StateMachine__states' and key in self.__states + ('switch',):
            raise AttributeError('State is readonly!')
        else:
            return super(type(self), self).__setattr__(key, value)

"""
类修饰器，
状态池从传入之时，便只能从switch函数切换
特点：提供可靠状态继承，没有元类不兼容问题，目前最推荐
注意：若继承自没有被本装饰器装饰的类，应确保它没有同时有states、switch、以及states中所有的属性
"""
def stateDefine(*states):
    _illegal_(states)
    keywords = states + ('switch', 'state', 'states')
    def dec(cls: type):
        inherite = hasattr(cls, 'states') and hasattr(cls, 'switch') and hasattr(cls, 'state') and _illegal_(getattr(cls, 'states'))
        for state in states:
            assert isinstance(state, str), 'State must be string'
            if inherite:
                if state in cls.states:
                    raise ValueError('Repeat state detected.')
            setattr(cls, state, f'{cls}.{state}')
        @property
        def __getstates(self):
            return states
        cls.states = cls.states + states if inherite else states
        new_setattr = None
        new_init_subclass = None
        new_delattr = None
        if '__setattr__' in cls.__dict__:
            origin_setattr = cls.__setattr__
            def _readonlify__setattr__(self, key, value):
                nonlocal states
                if key in states + ('switch', 'state'):
                    raise AttributeError('State\swtich is readonly!')
                else:
                    return origin_setattr(self, key, value)
            new_setattr = _readonlify__setattr__
        else:
            def _object__setattr(self, key, value):
                nonlocal states
                if key in states + ('switch', 'state'):
                    raise AttributeError('State\swtich is readonly!')
                else:
                    return object.__setattr__(self, key, value)
            new_setattr = _object__setattr
        if '__delattr__'  in cls.__dict__:
            origin_delattr = cls.__delattr__
            def __new_delattr__(self, key):
                if key in keywords:
                    raise AttributeError('State cannot be deleted!')
                origin_delattr(self, key)
            new_delattr = __new_delattr__
        else:
            def __object_delattr__(self, key):
                if key in keywords:
                    raise AttributeError('State cannot be deleted!')
                object.__delattr__(self, key)
            new_delattr = __object_delattr__
        def _switch(self, name: str):
            nonlocal states
            if isinstance(name, str):
                if name in cls.states:
                    self.__state = getattr(cls, name)
                else:
                    raise ValueError('No such state to switch!')
            else:
                raise TypeError("Str is expected.")

        @property
        def state(self):
            try:
                return self.__state
            except AttributeError:
                raise AttributeError("No state on the object. Please switch a state first!")

        if '__slots__' in cls.__dict__:
            cls.__slots__.append('__state')
            """
            若继承自父类也被此函数装饰，则父类会将其去掉
            """
        cls.state = state
        cls.__setattr__ = new_setattr
        cls.switch = _switch
        return cls
    return dec

__all__ = ['stateDefine', 'StateMachine']