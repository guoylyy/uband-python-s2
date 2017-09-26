# -*- coding: utf-8 -*-
import pygame

MOU_CON = True

board = pygame.Rect(280,400,80,5) #代表弹球版的方块
circle = [100,100] #球的半径
Radius = 10 #球半径
SPEED = [5,-5]#[dx,dy]每一帧移动的速度5个像素点
WIDTH = 640#屏幕宽度
HEIGHT = 480#屏幕高度

def renew_ball():
    if circle[1] > HEIGHT:
        circle[0] = 100
        circle[1] = 100
 
def update_ball():
    if circle[1] - Radius == 0:
        SPEED[1] *= -1
    if circle[0] + Radius == WIDTH or circle[0] - Radius == 0:
        SPEED[0] *= -1
    if circle[1] + Radius == board.top:#board.top也可以
        if circle[0] >= board.left and circle[0] <= (board.left+80):#或者board.right
            SPEED[1] *= -1

    circle[0] += SPEED[0]#0——即x坐标
    circle[1] += SPEED[1]#1——即y坐标



def draw_surface(screen):
    screen.fill([255,255,255]) #R G B white 如果没有则每一帧都是上一帧的叠加（连续路径）
    pygame.draw.circle(screen,[255,0,0],circle,Radius)
    pygame.draw.rect(screen,[0,255,255],board)
    pygame.display.flip()

def update_board():
    if MOU_CON:
        (x,y) = pygame.mouse.get_pos()#获取鼠标的位置信息
        board.centerx = x

def w_down_cb():
    pass

def s_down_cb():
    pass

def a_down_cb():
    if not MOU_CON:
        board.centerx -= 5

def d_down_cb():
    if not MOU_CON:
        board.centerx += 5

def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH,HEIGHT])
    running = True

    while running:
        pygame.time.delay(50)#50ms，不然画面闪的很快
        update_board()#根据鼠标输入更新弹球版的位置
        update_ball()
        draw_surface(screen)#在画布上绘画
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    w_down_cb()#call back 回调
                elif event.key == pygame.K_s:
                    s_down_cb()
                elif event.key == pygame.K_a:
                    a_down_cb()
                elif event.key == pygame.K_d:
                    d_down_cb()
        renew_ball()
    pygame.quit()

if __name__ == '__main__':
    main()