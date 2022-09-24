import pygame
from classes.media.audio import plane_audio, button_audio, bullet_audio
# 菜单背景音乐
menubgm = pygame.mixer.Sound('media/audio/game/bg/menubg.mp3')
# 游戏背景音乐
gamebgm = pygame.mixer.Sound('media/audio/game/bg/gamebg1.mp3')
gamebgm.set_volume(0.5)

# ready go
readygos = pygame.mixer.Sound('media/audio/game/bg/readygo/readygo.mp3')

# bullet audio
shoot1 = pygame.mixer.Sound('media/audio/bullet/shoot/shoot1.mp3')
shoot1.set_volume(0.7)
hitenemy1 = pygame.mixer.Sound('media/audio/bullet/shoot/shoot1.mp3')
hitenemy1.set_volume(2)
lionbullet_audio = bullet_audio.Bullet_Audio(shoot1, hitenemy1)

# booms
playerboom1 = pygame.mixer.Sound('media/audio/plane/boom/player/playerboom1.mp3')
lion_audio = plane_audio.Plane_Audio(playerboom1)

enemyboom1 = pygame.mixer.Sound('media/audio/plane/boom/enemy/enemyboom1.mp3')
sa_1_audio = plane_audio.Plane_Audio(enemyboom1)

# begin_button ui
read_grandfather_on_cover = pygame.mixer.Sound('media/audio/game/button/begin_button/button_on_cover.wav')
read_grandfather_on_click = pygame.mixer.Sound('media/audio/game/button/begin_button/button_on_click.wav')
read_grandfather_audio = button_audio.Button_Audio(read_grandfather_on_cover, read_grandfather_on_click)

# confirm grandfather button
confirm_grandfather_on_cover = pygame.mixer.Sound('media/audio/game/button/grandfather/confirm/on.wav')
confirm_grandfather_on_click = pygame.mixer.Sound('media/audio/game/button/grandfather/confirm/c.mp3')
confirm_grandfather = button_audio.Button_Audio(confirm_grandfather_on_cover, confirm_grandfather_on_click)

# cancel grandfather button
cancel_grandfather_on_cover = pygame.mixer.Sound('media/audio/game/button/grandfather/cancel/on.wav')
cancel_grandfather_on_click = pygame.mixer.Sound('media/audio/game/button/grandfather/cancel/c.wav')
cancel_grandfather = button_audio.Button_Audio(cancel_grandfather_on_cover, cancel_grandfather_on_click)

# grandfather frame
grandfather_frame_on_cover = pygame.mixer.Sound('media/audio/game/button/grandfather/grandframe/on.wav')
grandfather_frame_on_click = pygame.mixer.Sound('media/audio/game/button/grandfather/grandframe/c.mp3')
grandfather_frame = button_audio.Button_Audio(grandfather_frame_on_cover, grandfather_frame_on_click)




