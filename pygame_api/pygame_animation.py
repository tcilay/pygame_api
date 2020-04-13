#!/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay -- 
# -- date:2020/4/12 --
import sys
import pygame
from pygame.locals import *

# 屏幕每秒刷新的次数（帧率）
FPS = 33
# 白色
WHITE = (255, 255, 255)
# 初始位置
IMG_Y = 10
IMG_X = 10

pygame.init()

# 获得时钟
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("pygame animation")
img = pygame.image.load("../images/pygame.png")
# 缩小图片
img = pygame.transform.scale(img, (150, 150))

# 初始化图片移动的方向
direction = "right"

# 主循环
while True:

    # 每次都要重新绘制背景色
    screen.fill(WHITE)
    if direction == "right":
        IMG_X += 5
        if IMG_X == 350:
            direction = "down"
    elif direction == "down":
        IMG_Y += 5
        if IMG_Y == 350:
            direction = "left"
    elif direction == "left":
        IMG_X -= 5
        if IMG_X == 10:
            direction = "up"
    elif direction == "up":
        IMG_Y -= 5
        if IMG_Y == 10:
            direction = "right"

    # 绘制图片到坐标上
    screen.blit(img, (IMG_Y, IMG_X))

    for event in pygame.event.get():
        if event.type == QUIT:
            # 退出游戏
            pygame.quit()
            # 退出系统
            sys.exit()
        # 绘制屏幕
        pygame.display.update()

    # 刷新屏幕
    pygame.display.update()

    # 设置刷新频率
    fpsClock.tick(FPS)
