# -*- coding:utf-8 -*-

import pygame
# 游戏的初始化
pygame.init()

# 创建游戏的窗口 480*700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1>加载图像数据到内存
bg = pygame.image.load("./images/background.png")
# 2>使用游戏屏幕对象调用blit()方法将图像绘制到制定位置
screen.blit(bg, (0, 0))
# 3>调用pygame.display.update()更新整个屏幕的显示
# pygame.display.update()

# 绘制飞机图片
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))
# pygame.display.update()


# 可以在所有绘制工作完成后,统一调用update方法
pygame.display.update()

# 1>绘制初始飞机的位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建时钟对象
clock = pygame.time.Clock()

# 游戏循环 ->意味着游戏的正式开始

while True:
    # 可以制定时钟对象内部代码执行的频率
    clock.tick(1)
    # 2> 修改飞机的位置
    hero_rect.y -= 50
    # 判断飞机的位置
    if hero_rect.y <= 0:
        hero_rect.y = 700
    # 3> 调用blit方法绘制图像
    screen.blit(bg, (0, 0))  # 目的是为了覆盖飞机移动时的残影
    screen.blit(hero, hero_rect)
    # 4> 调用update方法更新显示
    pygame.display.update()


pygame.quit()
