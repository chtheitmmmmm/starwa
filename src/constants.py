import socket

from esign.tools.vector2 import Vector2

constants = {
    "meta": {
        "version": 0.5,
        "icon": "icon.ico",
        "FPS": 60,
        "caption": "星野守望",
        "windowSize": [640, 797],
        'net': {
            "server": (
                "localhost",
                9800
            ),
            'family': socket.AF_INET,  # ipv4
            'type': socket.SOCK_STREAM,  # TCP连接,
            'encoding': 'utf-8',
            'protocol': {
                'typecode': {  # 对象的代号
                    "player": {
                        "lion": 1,
                        "bird": 2,
                    },
                    "enemy": {
                        "sa_1": 1,
                        "sc_1": 2,
                        "sc_2": 3,
                        "sc_3": 4,
                        "sc_4": 5
                    },
                },
            },
        }
    },
    "plane": {
        "player": [{
            "nameitem": "lion"
        }, {
            "nameitem": "bird"
        }],
        "enemy": {
            # name and its code
            'sa_1': 0,
            'sc_1': 1,
            'sc_2': 2,
            'sc_3': 3,
            'sc_4': 4
        }
    },
    "bg": {
        "fightsinglepg": {
            "speed": Vector2(0, 2)
        }
    },
    "locations": {
        "planeInitialVertical": 550,
        'arw': Vector2(50, 100),
    }
}

__all__ = ['constants']
