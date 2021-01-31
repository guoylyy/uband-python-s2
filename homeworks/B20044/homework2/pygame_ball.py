# -*- coding: utf-8 -*-
import pygame


MOU_CON = True

#保存屏幕的宽高 好处是想改相关参数的话，第一行改就可以了
WIDTH = 640
HEIGHT = 480

#定义全局变量

board = pygame.Rect(280, 400, 80, 5)
#board是rect类的一个实例对象
#board的上边缘：board.top
#board的左边缘：board.left
#board的右边缘：board.right


circle = [100, 100]
RADIUS = 10

#小球速度
SPEED = [5, -5]#每个单位时间走5个像素点  小球往上边跑


#让球动
def update_ball():#根据小球速度更新小球位置

#   让球动 → 小球移动后的坐标
    circle[0] += SPEED[0]#小球现在x轴位置=原本x轴坐标+运行速度   circle[0] =  circle[0]+ SPEED[0]
    circle[1] += SPEED[1]#小球现在y轴位置=原本y轴坐标+运行速度

    #1.遇到边缘回弹

    #1）上边缘
    if circle[1] - RADIUS == 0: #当球撞到上边缘时，圆心的纵坐标（正）=半径
        SPEED[1] *= -1  #小球反向运行 原来y坐标是向上-5，现在y坐标*-1为5
    #2)右边缘+左边缘
    if circle[0] + RADIUS >= WIDTH or circle[0] - RADIUS <= 0:
        SPEED[0] *= -1

    # 2.遇到板回弹
    # 圆心+半径=小板的上边缘 圆心的x轴在小板的范围之内
    if (circle[1] + RADIUS == board[1]) and (board[0]<=circle[0]<=(board[0]+board[2])):
        #                                   板左上角横坐标<=球心x<=板右上角横坐标
        #注意中间是==，写成=运行错误，rect[1]也不能运行
        SPEED[1] *= -1
    else:
        return True




#画球和板
def draw_surface(screen):
    #如果不重新填充，上一次画的东西就还在
    screen.fill([255, 255, 255])  # R G B white
    pygame.draw.circle(screen, [255, 0, 0], circle, RADIUS)
    pygame.draw.rect(screen, [0, 255, 255], board)

    pygame.display.flip()
#让板动
def update_board():
    if MOU_CON:
        (x, y) = pygame.mouse.get_pos()
        board.centerx = x #只控制板左右移动


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
    screen = pygame.display.set_mode([WIDTH, HEIGHT])#改成width和height
    running  = True

    while running:
        pygame.time.delay(50) # 50ms毫秒  每次循环都稍微延迟一段时间，否则一闪而过
        #画板和球
        draw_surface(screen)

        #板动
        update_board()
        
        #球动
        update_ball()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    w_down_cb()
                elif event.key == pygame.K_s:
                    s_down_cb()
                elif event.key == pygame.K_a:
                    a_down_cb()
                elif event.key == pygame.K_d:
                    d_down_cb()
    pygame.quit()

if __name__ == '__main__':
    main()
