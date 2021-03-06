#!/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay -- 
# -- date:2020/4/12 --
import sys
import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
# 窗口
screen = pygame.display.set_mode((500, 500))
# 窗口标题
pygame.display.set_caption('do pygame font')

# 获取字体
fontObj = pygame.font.Font("../font/simsun.ttc", 20)

# 设置显示文字
txt = fontObj.render("pygame font", True, BLUE, GREEN)
# 获取rect
txtRect = txt.get_rect()
# 设置坐标
txtRect.center = (250, 200)
# 绘制背景
screen.fill(WHITE)
# 绘制字体
screen.blit(txt, txtRect)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            # 退出游戏
            pygame.quit()
            # 退出系统
            sys.exit()
        # 绘制屏幕
        pygame.display.update()
