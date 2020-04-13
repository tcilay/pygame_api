#!/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay -- 
# -- date:2020/4/12 --
import sys
import pygame
from pygame.locals import *
from math import pi

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
# 窗口
screen = pygame.display.set_mode((500, 500))
# 窗口标题
pygame.display.set_caption('do pygame_api draw')

# 背景颜色
screen.fill(WHITE)

""" 线段
    (screen, BLACK, [0, 0], [40, 40], 50)
    (画布,颜色,起点,终点,宽度)
"""
pygame.draw.line(screen, BLACK, [0, 40], [40, 40], 3)
""" 抗锯齿线"""
pygame.draw.aaline(screen, RED, [50, 50], [150, 50], 1)
""" 折线 不闭合"""
pygame.draw.lines(screen, RED, False, [[0, 80], [20, 90], [250, 80], [220, 30]], 3)
""" 空心矩形"""
pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 5)
""" 实心矩形"""
pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])
""" 空心椭圆"""
pygame.draw.ellipse(screen, BLUE, [230, 10, 50, 20], 3)
""" 实心椭圆 [x轴,y轴,宽,高]"""
pygame.draw.ellipse(screen, BLUE, [300, 10, 100, 50])
""" 多边形"""
pygame.draw.polygon(screen, GREEN, [[100, 100], [0, 200], [200, 200], [130, 180]], 3)

""" 弧线"""
pygame.draw.arc(screen, GREEN, [250, 250, 150, 125], 0, pi / 2, 3)
pygame.draw.arc(screen, BLACK, [250, 250, 150, 125], pi / 2, pi, 3)
pygame.draw.arc(screen, RED, [250, 250, 150, 125], pi, 3 * pi / 2, 3)
pygame.draw.arc(screen, BLUE, [250, 250, 150, 125], 3 * pi / 2, 2 * pi, 3)

""" 空心圆"""
pygame.draw.circle(screen, BLUE, [80, 400], 50, 5)
""" 实心圆"""
pygame.draw.circle(screen, BLUE, [80, 280], 50)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            # 退出游戏
            pygame.quit()
            # 退出系统
            sys.exit()
        # 绘制屏幕
        pygame.display.update()
