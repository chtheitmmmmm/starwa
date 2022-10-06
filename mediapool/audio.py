from esign import *

ap = AudioPool('media/audio')
ap.registers({
    'bg': [
        'bg/fight.mp3',
        'bg/menu.mp3',
        'bg/readygo.mp3',
        'bg/select.mp3',
        'bg/loading_1.mp3',
        'bg/loading_2.mp3',
        'bg/loading_3.mp3'
    ],
    'bullet': {
        'boom': [
            'bullet/boom/hitenemy1.wav',
            'bullet/boom/hitenemy2.wav',
        ],
        'shoot': [
            'bullet/shoot/shoot1.mp3',
        ]
    },
    'button': {
        'menupg': [
            'button/begin_button/button_on_click.wav',
            'button/begin_button/button_on_cover.wav'
        ],
        'equip': [
            'button/equip/equip.mp3'
        ],
        'arw': [
            'button/select_arw/plane_arw.mp3'
        ],
        'back': [
            'button/back_fight/back.mp3'
        ],
        'fight': [
            'button/back_fight/fight.mp3'
        ]
    },
    'plane': {
        'boom': {
            'enemy': [
                'plane/boom/enemy/enemyboom1.mp3',
                'plane/boom/enemy/enemyboom2.wav'
            ],
            'player': [
                'plane/boom/player/playerboom1.mp3',
                'plane/boom/player/playerboom2.wav'
            ]
        },
        'sentence': {
            'player': {
                'bird': [
                    'plane/sentence/player/bird/bird.mp3',
                    'plane/sentence/player/bird/bird2.mp3'
                ],
                'lion': [
                    'plane/sentence/player/lion/lion.mp3',
                    'plane/sentence/player/lion/lion2.mp3'
                ]
            }
        }
    }
})



__all__ = ['ap']

