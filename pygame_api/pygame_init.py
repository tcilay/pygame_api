#!/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay -- 
# -- date:2020/4/12 --
import sys
import pygame
from pygame.locals import *

# 初始化pygame
pygame.init()
# 初始化窗口大小
screen = pygame.display.set_mode((500, 500))
# 标题
pygame.display.set_caption("初始化练习")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            # 退出游戏
            pygame.quit()
            # 退出系统
            sys.exit()
        # 绘制屏幕
        pygame.display.update()


