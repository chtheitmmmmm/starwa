def platDict(D: dict):
    plat = {}
    queue = [D]
    while queue:
        d = queue.pop()
        for key, value in d.items():
            if isinstance(value, dict):
                queue.append(value)
            plat[key] = value
    return plat


def recursiveDict(D: dict):
    """
    递归字典。比如：
    @recursiveDict({
        'a': {
            'b': 100
        },
        'c': {
            'd': {
                'e': 200
            }
        }
    })
    class foo:
        pass
    a = foo()
    a['c']  # ==> { 'd': { 'e' : 200 } }
    a['e']  # ==> 200
    a['b']  # ==> 100
    ================
    attention: 如果传入的字典有重复的键，后值将覆盖前值
    """
    assert isinstance(D, dict), 'A dict expected!'
    plat = platDict(D)
    def dec(cls: type):
        new_getitem = None
        if '__getitem__' in dir(cls):
            origin_getitem = cls.__getitem__
            def __getitem__(self, key):
                if key in plat:
                    return plat[key]
                else:
                    return origin_getitem(self, key)
            new_getitem = __getitem__
        else:
            def __getitem__(self, key):
                return plat[key]
            new_getitem = __getitem__
        cls.__getitem__ = new_getitem
        return cls
    return dec

__all__ = ['platDict', 'recursiveDict']