# -*- coding: utf-8 -*-
# author:huafeng 
#完善 贪吃蛇游戏-重新生成苹果，蛇不能掉头，蛇吃到自己失败，显示图片

import pygame
import random
import os


SCALE = 20   # 屏幕是 20*20 个格子
SIZE = 20     # 每个格子是 20个像素

WIDTH = SCALE * SIZE     # 窗口的宽度
HEIGHT = SCALE * SIZE    # 窗口的高度
DIRECT = [[0,-1],[-1,0],[0,1],[1,0]]     # 定义4个方向，上，左，下，右方便后续
dirt = 1 
apple = [10,8]                   # 定义 苹果的初始位置

snake = [[9,3],[10,3],[11,3]]  #定义 蛇的初始化位置

# 蛇前进1格后，插入蛇头新的坐标列表，如果不变长，则删除最后一个列表。变长则不删除。

# 更新蛇的运动状态
def update_snake():
    new_body = [0,0]               #定义一个蛇的新蛇头列表
    new_body[0] = (snake[0][0] + DIRECT[dirt][0]) % SCALE  # 新身体的X矩阵坐标为蛇头X+方向X运算，当为-1等时，等于从列表后面向前走。
    new_body[1] = (snake[0][1] + DIRECT[dirt][1]) % SCALE # 新身体的X矩阵坐标为蛇头Y+方向Y运算，当为-1等时，等于从列表后面向前走。
    if new_body == apple:         # 当 蛇头 到达苹果位置时
        snake.insert(0,new_body)  # 插入新的蛇头
        return True
    else:
        snake.insert(0,new_body)  # 插入新的 蛇头
        snake.pop()                 # 删除尾巴最后一个
        return False

# 显示窗口蛇身 相关特性
def screen_display(screen):                #
    screen.fill([255, 255, 255])           #画一个白色的窗口
    pygame.draw.rect(screen,[0,0,255],[snake[0][0]*SIZE,snake[0][1]*SIZE,SIZE - 1,SIZE - 1])  # 蛇头标记为蓝色
    # index = 1
    for body in snake[1:]:
            pygame.draw.rect(screen,[0,255,0],[body[0]*SIZE,body[1]*SIZE,SIZE - 1,SIZE - 1])  #方框左，上，宽，厚
    img = pygame.image.load('redapple1.jpg')  #图片路径，一般和python源文件放在一个目录下
    screen.blit(img,[apple[0]*SIZE,apple[1]*SIZE])
    pygame.display.flip()         #显示到窗口中

def new_apple():
    apple[0] = random.randint(0,19)
    apple[1] = random.randint(0,19)

# 吃自己
def eat_self():
    if snake.count(snake[0]) >= 2:
        return True
    return False

def gameover(screen):
    running  = True 
    while running:
        screen.fill([255, 255, 255])
        font = pygame.font.Font(None,32)
        text = font.render('game over',True,[255,0,0])
        screen.blit(text,[7*SIZE,7*SIZE])
        pygame.display.flip()
        for event in pygame.event.get():        
            if event.type == pygame.QUIT:        
                running = False  
    pygame.quit()     


# 按键响应  防止贪吃蛇 掉头
def w_down_cb():
    global dirt
    if dirt % 2 != 0:    #  当前方向 为左 或 右，才方向上
        dirt = 0
def s_down_cb():    #  #  当前方向 为左 或 右，才方向下
    global dirt
    if dirt % 2 != 0:
        dirt = 2
def a_down_cb():   #  #  当前方向 为上 或 下，才方向左
    global dirt
    if dirt % 2 != 1:
        dirt = 1
def d_down_cb():   #  #  当前方向 为上 或 下，才方向右
    global dirt
    if dirt % 2 != 1:
        dirt = 3

def main():
    pygame.init()                       # 对Pygame 进行初始化              
    screen = pygame.display.set_mode([WIDTH, HEIGHT])        # 定义 一定大小的窗口
    running  = True                         # 运行条件
    # new_apple = [random.randint(1,20),random.randint(1,20)]    #随机定义坐标
    while running:
        pygame.time.delay(200)   # 50ms  延迟
        if update_snake():
            new_apple()

        if eat_self():
            gameover(screen)
            break


        screen_display(screen)  # 调用显示程序
        # update_apple(new_snake,screen,snake,new_apple)      # 
        for event in pygame.event.get():          # 获取键盘响应
            if event.type == pygame.QUIT:         # 退出 响应
                running = False
            elif event.type == pygame.KEYDOWN:    # 获得键盘响应
                if event.key == pygame.K_w:        # 上
                    w_down_cb()
                elif event.key == pygame.K_s:      # 下
                    s_down_cb()
                elif event.key == pygame.K_a:      # 左
                    a_down_cb()
                elif event.key == pygame.K_d:       # 右
                    d_down_cb()
    pygame.quit()

if __name__ == '__main__':
    main()



    # for body in snake:
    #     body[1] = body[1] + SPEEDy[1]

# def renew_ball():
#     if circle[1] > HEIGHT:
#         circle[0] = 100
#         circle[1] = 100

# def update_ball():
#     if circle[1] - RADIUS == 0:
#         SPEED[1] *= -1
#     if circle[0] + RADIUS == WIDTH or circle[0] - RADIUS == 0:
#         SPEED[0] *= -1

#     if circle[1] + RADIUS == board.top and circle[0] > board.left and circle[0] < board.right:
#         SPEED[1] *= -1

    # circle[0] += SPEED[0]
    # circle[1] += SPEED[1]


# def draw_surface(screen):
#     screen.fill([255, 255, 255])  # R G B white
#     pygame.draw.circle(screen, [255, 0, 0], circle, RADIUS)
#     pygame.draw.rect(screen, [0, 255, 255], board)
#     pygame.display.flip()

# def update_board():
#     if MOU_CON:
#         (x, y) = pygame.mouse.get_pos()
#         board.centerx = x