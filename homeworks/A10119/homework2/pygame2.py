# -*- coding: utf-8 -*-
import pygame

MOU_CON = True

board = pygame.Rect(280,400,80,5) #代表弹球版的方块
circle = [100,100] #球的半径
Radius = 10 #球半径

def draw_surface(screen):
    screen.fill([255,255,255]) #R G B white
    pygame.draw.circle(screen,[255,0,0],circle,Radius)
    pygame.draw.rect(screen,[0,255,255],board)
    pygame.display.flip()

def update_board():
    if MOU_CON:
        (x,y) = pygame.mouse.get_pos()#获取鼠标的位置信息
        board.centerx = x
        board.centery = y

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
    screen = pygame.display.set_mode([640,480])
    running = True

    while running:
        update_board()#根据鼠标输入更新弹球版的位置
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
    pygame.quit()

if __name__ == '__main__':
    main()