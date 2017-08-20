# -*- coding: utf-8 -*-
import pygame

MOU_CON = True
WIDTH = 640
HEIGHT = 480

board = pygame.Rect(280, 400, 80, 5) #代表弹球板的方块
circle = [100, 100] #球的圆心位置
RADIUS = 10 #球半径
SPEED = [1, -1] #球的速度


def draw_surface(screen):
    screen.fill([255, 255, 255])  # R G B white
    pygame.draw.circle(screen, [255, 0, 0], circle, RADIUS)
    pygame.draw.rect(screen, [0, 255, 255], board)
    pygame.mouse.set_visible(False)
    pygame.display.flip()

def update_ball():
    # 碰壁检测
    if circle[1] - RADIUS == 0:
        SPEED[1] *= -1
    if circle[0] - RADIUS == 0 or circle[0] + RADIUS == WIDTH:
        SPEED[0] *= -1
    # 碰板子检测
    if circle[0] >= board.left and circle[0] <= board.right and circle[1] + RADIUS == board.top:
        SPEED[1] *= -1

    circle[0] += SPEED[0]
    circle[1] += SPEED[1]

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

def correct_board_pos():
    if board.left <= 0:
        board.left = 0
    if board.right >= WIDTH:
        board.right = WIDTH

def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    running  = True

    while running:
        pygame.time.delay(7)
        update_board()  #根据鼠标输入更新弹球板的位置
        update_ball()
        for event in pygame.event.get():
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
        correct_board_pos()
        draw_surface(screen)  # 在画布上绘画
    pygame.quit()

if __name__ == '__main__':
    main()