import pygame


# 游戏版本
version = '0.3'

# 窗口尺寸
SCREEN_SIZE  = (640, 797)

# 存档条尺寸
GRAND_SIZE = (463, 120)

# 帧率
FPS = 60

# 最多存档数
GRAND_NUM_MAX = 9


# 一些小函数
def get_interval(size, speed, frame_rate=FPS):
    return int(size[1] / abs(speed[1]) * 1 / FPS * 1000)

# 飞机起始位置纵坐标固定
BeginLocCEnter = 550
# HP条位置
LocHp = (120, 700)

# 飞机图片尺寸
PLAYER_SIZE = (128, 128)

# 飞机武器参数常量
# 尺寸
LionBulletSize = [20, 40]
# 速度
LionBulletSpeed = [0, -8]
LionBulletAcce  = [0, -0.5]
# 时间间隔
LionBulletInterval = get_interval(LionBulletSize, LionBulletSpeed)
# 空间间隔
LionGunInterval = (1/6, 2/3)

# 敌机武器参数常量
# 尺寸
sa_1BulletSize = [30, 30]
# 速度
sa_1BulletSpeed = [0, 3]
sa_1BulletAcce = [0, 0.1]
# 时间间隔
sa_1BulletInterval = 1000
# 空间间隔
sa_1GunInterval = (1/3,)



# 各种飞机的HP值
LionHp = 100
sa_1Hp = 100