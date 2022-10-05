from src.starwarapp import StarwarApp
from src.constants import constants
from esign.page import Pages

"""
初始化应用程序，尚不存在页面
"""
pages = Pages()

starwar = StarwarApp(
    pages     = pages,
    constants = constants
)

from mediapool import *
from pages import *

starwar.add_page(
    name = 'menupg',
    page = menupg
)

starwar.add_page(
    name = 'selectpg',
    page = selectpg
)

starwar.add_page(
    name = 'fightsinglepg',
    page = fightsinglepg
)

starwar.add_page(
    name = 'loadingpg',
    page = loadingpg
)

starwar.add_page(
    name = 'fightmultiplepg',
    page = fightmultiplepg
)

starwar.entry('menupg')     # 设置入口页面
starwar.run()               # 开始运行