# -*- coding: utf-8 -*-
import pygame
MON_CON = True
width = 180
height = 5
board = pygame.Rect(280,400,width,height) #弹球方块

circle = [100,100] #圆心位置
RADIUS = 10 #球半径
SPEED = [5,5] #每个单位时间走5个像素点
WIDTH = 640
HEIGHT = 480

def update_ball():
    if circle[1] - RADIUS == 0:
        SPEED[1] *= -1
    if (circle[0] +RADIUS == WIDTH) or (circle[0] - RADIUS ==0):
        SPEED[0] *=-1
    if (circle[1]+RADIUS +height/2 ==board.centery) and ((-width/2) < (circle[0]-board.centerx) < (width/2)):
        SPEED[1] *= -1

    circle[0] += SPEED[0]
    circle[1] -= SPEED[1]



def draw_surface(screen):
    screen.fill([255, 255, 255]) #R G B white 每一次都要重新填充否则就变成每一帧的叠加
    pygame.draw.circle(screen, [255, 0, 0], circle, RADIUS)  # 0球 1圆环 默认0
    pygame.draw.rect(screen, [0, 255, 255], board)  # 0实心 1或其他边框厚度
    pygame.display.flip() #显示到界面上
def update_board():
    if MON_CON:
        (x,y) = pygame.mouse.get_pos() #获取鼠标的位置信息
        board.centerx = x #板的x随鼠标移动
        #board.centery = y
def w_down_cb():
    if not MON_CON:
        (x,y) = pygame.mouse.get_pos()
       # board.centery -= 5 #pygame的坐标系和传统的是反向的 第四象限。
        pass
def a_down_cb():
    if not MON_CON:
        (x,y) = pygame.mouse.get_pos()
        board.centerx -= 15
def s_down_cb():
    if not MON_CON:
        (x,y) = pygame.mouse.get_pos()
       # board.centery += 5
        pass
def d_down_cb():
    if not MON_CON:
        (x,y) = pygame.mouse.get_pos()
        board.centerx += 15

def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH,HEIGHT]) #分辨率 返回screen操作变量
    running = True

    while running:
        pygame.time.delay(50)
        update_board() #根据鼠标的输入更新弹球的位置
        update_ball()
        draw_surface(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    w_down_cb()#call back 回调函数 对按键的相应
                elif event.key == pygame.K_s:
                    s_down_cb()
                elif event.key == pygame.K_a:
                    a_down_cb()
                elif event.key == pygame.K_d:
                    d_down_cb()
    pygame.quit()
if __name__ == '__main__':
	main()