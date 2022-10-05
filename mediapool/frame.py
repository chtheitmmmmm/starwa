from esign import *
from src.constants import constants
fps = constants['meta']['FPS']

fp = FramePool('media/graphic')
fp.registers({
    'bg': {
        'menupg': [{
            f"bg/menubg/{i}.jpg": 6
        } for i in range(1, 30)],
        'battle': [{
            'bg/battlebg/map_1.jpg': 1
        }],
        'title': [{
            f"bg/title/title.png": 1
        }],
        'readygo': {
            'ready': [{
                f"bg/readygo/ready/{i}.png": 10
            } for i in range(1, 6)],
            'go': [{
                f"bg/readygo/go/{i}.png": 10
            } for i in range(5, 0, -1)]
        },
        'select': [{
            'select/bg.jpg': 1
        }],
        'nameframe': [{
            'select/name.png': 1
        }],
        'bottom': [{
            'select/bottom.png': 1
        }],
        'loading': {
            'bg': [{
                f'loading/bg{i}.jpg': 5 * fps
            } for i in range(1, 4)],
            'loading': [{
                f'loading/l{i}.png' : 5
            } for i in range(1, 5)]
        }
    },
    'plane': {
        'boom': {
            'player': [{
                f'planes/boom/player/boom1/{i}.png' : 5
            } for i in range(1, 10)],
            'enemy': [{
                f'planes/boom/enemy/boom2/{i}.png' : 5
            } for i in range(1, 10)]
        },
        'hp': {
            'bar': {
                'enemy': [{
                    'planes/hp/bar/enemy/bar.png': 1
                }],
                'player': [{
                    'planes/hp/bar/player/bar.png': 1
                }]
            },
            FRAME: {
                'enemy': [{
                    'planes/hp/frame/enemy/frame.png': 1
                }],
                'player': [{
                    'planes/hp/frame/player/frame.png': 1
                }]
            },

        },
        'apperance': {
            'enemy': [{
                'planes/apperance/enemy/soldier/sa_1.png' : 1
            }, {
               'planes/apperance/enemy/soldier/sc_1.png' : 1
            }, {
                'planes/apperance/enemy/soldier/sc_2.png' : 1
            }, {
                'planes/apperance/enemy/soldier/sc_3.png' : 1
            }, {
                'planes/apperance/enemy/soldier/sc_4.png' : 1
            }],
            'player': {
                'lion': {
                    'nameitem': [{
                        f'select/ln{i}.png': 5,
                    } for i in range(1, 4)],
                    'people': [{
                        f'select/l{i}.png': 5
                    } for i in range(1, 4)],
                    'plane': [{
                        'planes/apperance/player/lion/l1.png' : 1
                    }, {
                        'planes/apperance/player/lion/l2.png' : 1
                    }, {
                        'planes/apperance/player/lion/l3.png' : 1
                    }, {
                        'planes/apperance/player/lion/ord.png' : 1
                    }, {
                        'planes/apperance/player/lion/r1.png' : 1
                    }, {
                        'planes/apperance/player/lion/r2.png' : 1
                    }, {
                        'planes/apperance/player/lion/r3.png' : 1
                    }]
                },
                'bird': {
                    'nameitem': [{
                        f'select/bn{i}.png': 5,
                    } for i in range(1, 4)],
                    'people': [{
                        f'select/b{i}.png': 5
                    } for i in range(1, 4)],
                    'plane': [{
                        'planes/apperance/player/bird/l1.png' : 1
                    }, {
                        'planes/apperance/player/bird/l2.png' : 1
                    }, {
                        'planes/apperance/player/bird/l3.png' : 1
                    }, {
                        'planes/apperance/player/bird/ord.png' : 1
                    }, {
                        'planes/apperance/player/bird/r1.png' : 1
                    }, {
                        'planes/apperance/player/bird/r2.png' : 1
                    }, {
                        'planes/apperance/player/bird/r3.png' : 1
                    }],
                },
            }
        },
        'bullet': {
            'enemy': {
                'red': [{
                    'planes/weapon/enemy/red/red.png': 1
                }, {
                   'planes/weapon/enemy/red/effect/1.png': 5
                }, {
                   'planes/weapon/enemy/red/effect/2.png': 5
                }, {
                   'planes/weapon/enemy/red/effect/3.png': 5
                }]
            },
            'player': {
                'blue': {
                    'bar': [{
                        'planes/weapon/player/blueweapon/bluebar.png': 1
                    }],
                    'point': [{
                        'planes/weapon/player/blueweapon/bluepoint.png': 1
                    }],
                    'effect': [{
                        f'planes/weapon/player/blueweapon/effect/{i}.png' : 3
                    } for i in range(1, 5)]
                },
                'red': {
                    'bar': [{
                        'planes/weapon/player/redweapon/redbar.png': 1
                    }],
                    'point': [{
                        'planes/weapon/player/redweapon/redpoint.png': 1
                    }],
                    'effect': [{
                        f'planes/weapon/player/redweapon/effect/{i}.png': 3
                    } for i in range(1, 5)]
                }
            }
        }
    },
    'ui': {
        'button': {
            'mp': [{
                'ui/button/multiPlayer/ord.png': 1
            }, {
                'ui/button/multiPlayer/touch.png': 20
            }, {
                'ui/button/multiPlayer/click.png': 20
            }],
            'sp': [{
                'ui/button/singlePlayer/ord.png': 1
            }, {
                'ui/button/singlePlayer/touch.png': 20
            }, {
                'ui/button/singlePlayer/click.png': 20
            }],
            'lplane': [{
                'select/l_dis.png': 1,
            }, {
                'select/l_ord.png': 1,
            }, {
                'select/l_on.png': 1
            }],
            'nplane': [{
                'select/n_dis.png': 1,
            }, {
                'select/n_ord.png': 1,
            }, {
                'select/n_on.png': 1
            }],
            'back': [{
                'select/back_ord.png': 1,
            }, {
                'select/back_on.png': 20,
            }, {
                'select/back_click.png': 20
            }],
            'fight': [{
                'select/fight_ord.png': 1,
            }, {
                'select/fight_on.png': 20,
            }, {
                'select/fight_click.png': 20
            }]
        }
    }
})

__all__  = ['fp']