#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Liluo

import pygame
import time

MOU_CON = True
board = pygame.Rect(280, 400, 80, 5)
circle = [100, 100]
RADIUS = 10
SPEED=[5,5]
WIDTH=640
HEIGHT=480


def update_ball(score):
    circle[0]+=SPEED[0]
    circle[1]+=SPEED[1]
    if circle[1]-RADIUS<=0:
        SPEED[1]*=-1
    if circle[0]+RADIUS>=WIDTH or circle[0]-RADIUS<=0:
        SPEED[0]*=-1
    if (circle[0]>=board.left) and (circle[0]<=board.right)and(circle[1]+RADIUS>=board.top):
        SPEED[1]*=-1
        score+=10
    return score

def renew_ball(score):
    text1=""
    if circle[1]+RADIUS>HEIGHT:
        text1="GAME OVER! TRY AGAIN!"
        circle[0]=100
        circle[1]=100
        score=0
    return text1,score

def draw_surface(screen,score,text):
    yellow = (255, 255, 0)

    # create the basic window/screen and a title/caption
    # default is a black background

    pygame.display.set_caption("ball game")
    # pick a font you have and set its size
    myfont = pygame.font.SysFont("Comic Sans MS", 30)
    # apply it to text on a label
    label1 = myfont.render("Your Score:%d"%(score), 1, yellow)

    # put the label object on the screen at point x=100, y=100
    screen.fill([0, 0, 0])  #否则是所有帧的叠加
    pygame.draw.circle(screen,[255,0,0],circle,RADIUS)
    pygame.draw.rect(screen,[0,255,255],board)
    screen.blit(label1, (10, 100))# show the whole thing
    if text!="":
        label2 = myfont.render("%s" % (text), 1, yellow)
        screen.blit(label2, (10, 200))
        pygame.display.flip()
        time.sleep(6)
    else:
        pygame.display.flip()


def update_board():
    if MOU_CON:
        (x,y)=pygame.mouse.get_pos()
        board.centerx=x
        # board.centery=y

def w_down_cb():
    if not MOU_CON:
        board.centery-=5

def s_down_cb():
    if not MOU_CON:
        board.centery+=5
def a_down_cb():
    if not MOU_CON:
        board.centerx+=5

def d_down_cb():
    if not MOU_CON:
        board.centerx-=5

def main():

    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])  # 生成游戏界面大小
    running = True
    SCORE=0
    while running:
        pygame.time.delay(50) #ms
        update_board() #根据鼠标输入更新板的位置
        (SCORE)=update_ball(SCORE)
        (text,SCORE)=renew_ball(SCORE)
        draw_surface(screen,SCORE,text)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    w_down_cb() #csll_back回调函数
                elif event.key==pygame.K_s:
                    s_down_cb()
                elif event.key==pygame.K_a:
                    a_down_cb()
                elif event.key==pygame.K_d:
                    d_down_cb()
    pygame.quit()


if __name__ == "__main__":
    main()