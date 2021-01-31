# -*- coding: utf-8 -*-
import pygame

MOU_CON = True

#board是rect类的一个实例对象
#边缘：board.top board.left board.right
board = pygame.Rect(280, 400, 80, 5) #代表弹球板的方块  左上x,y length width

circle = [100, 100] #球的圆心位置xy
RADIUS = 10 #球半径
SPEED = [5, 5]	# 球速

WIDTH = 640
HEIGHT = 480

def update_ball():
    # 上边缘
    if circle[1] - RADIUS == 0:
        SPEED[1] *= -1
    #板
    elif circle[1] + RADIUS == board.top and circle[0] < board.right and circle[0] > board.left:
        SPEED[1] *= -1
    # 左右边缘
    if circle[0] + RADIUS == WIDTH or circle[0] - RADIUS == 0:
        SPEED[0] *= -1

    circle[0] += SPEED[0]
    circle[1] += SPEED[1]


def draw_surface(screen):   #draw_component
    screen.fill([255, 255, 255])  # R G B white
    pygame.draw.circle(screen, [255, 0, 0], circle, RADIUS) #Panel,Color,Center,Radius
    pygame.draw.rect(screen, [0, 255, 255], board)  # Panel,Color,Rect
    pygame.display.flip()   # 绘制Panel

def update_board():
    if MOU_CON:
        (x, y) = pygame.mouse.get_pos() #获取鼠标的位置信息
        board.centerx = x

def w_down_cb():
    if not MOU_CON:
        board.centery -= 5

def s_down_cb():
    if not MOU_CON:
        board.centery += 5

def a_down_cb():
    if not MOU_CON:
        board.centerx -= 5

def d_down_cb():
    if not MOU_CON:
        board.centerx += 5

def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])    #Panel init
    running  = True     # 运行锁

    while running:
        pygame.time.delay(20) # 50ms
        update_board()  #根据输入更新弹球板的位置
        update_ball()
        draw_surface(screen)  #在画布上绘画
        for event in pygame.event.get():    # 获取事件
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    w_down_cb() # call_back 回调
                elif event.key == pygame.K_s:
                    s_down_cb()
                elif event.key == pygame.K_a:
                    a_down_cb()
                elif event.key == pygame.K_d:
                    d_down_cb()
    pygame.quit()

if __name__ == '__main__':
    main()