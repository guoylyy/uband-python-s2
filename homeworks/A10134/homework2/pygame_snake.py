#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Liluo

import pygame
import random
import datetime

SCALE=20 #格数
SIZE=20  #每一格的大小
WIDTH=SCALE*SIZE
HEIGHT=SCALE*SIZE

snake0 = [[4, 3], [5, 3], [6, 3]]
snake= [[4, 3], [5, 3], [6, 3]]

apple = [3, 1]

DIRECT=[[0,-1],[-1,0],[0,1],[1,0]]
dirt=1


yellow = (255, 255, 0)


def update_snake():
    new_body=[0,0]
    new_body[0]=(snake[0][0]+DIRECT[dirt][0])%SCALE
    new_body[1]=(snake[0][1]+DIRECT[dirt][1])%SCALE
    snake.insert(0,new_body)
    if new_body!=apple:
        snake.pop()


def update_apple():
    head = snake[0]

    if head==apple:
        apple[0]=random.randint(0, SCALE-1)
        apple[1]=random.randint(0,SCALE-1)

def screen_show(screen):
    global snake0, snake
    head = snake[0]

    screen.fill([255,255,255])
    if game_over()==0:
        bodies=snake[1:len(snake)+1]
        for body in bodies:
            pygame.draw.rect(screen,[0,255,0],[body[0]*SIZE,body[1]*SIZE,SIZE-1,SIZE-1])
        pygame.draw.rect(screen,[255,255,0],[head[0]*SIZE,head[1]*SIZE,SIZE-1,SIZE-1])
    else:
        myfont = pygame.font.SysFont("Comic Sans MS", 30)
        label = myfont.render("GAME OVER", 1, yellow)
        screen.blit(label, [10, 200])
        snake=snake0
        pygame.time.delay(1000)
    # pygame.draw.circle(screen,[255,0,0],(apple[0]*SIZE+SIZE/2,apple[1]*SIZE+SIZE/2),SIZE/2)
    img=pygame.image.load("th.png")
    screen.blit(img,[apple[0]*SIZE-1/2*SIZE,apple[1]*SIZE-1/2*SIZE])

    pygame.display.flip()

def w_down_cb():
    global dirt
    if (dirt-0)%2:
        dirt=0


def d_down_cb():
    global dirt
    if (dirt-3)%2:
        dirt=3

def a_down_cb():
    global dirt
    if (dirt-1)%2:
        dirt=1

def s_down_cb():
    global dirt
    if (dirt-2)%2:
        dirt=2

def game_over():
    head = snake[0]
    if_over=0
    count=0
    for body in snake:
        if body==head:
            count+=1
    if count>=2:
        if_over=1
    return if_over


def main():

    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])  # 生成游戏界面大小
    running = True

    while running:
        random.seed(datetime.datetime.now())
        pygame.time.delay(150) #ms
        update_snake()
        update_apple()
        screen_show(screen)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    w_down_cb() #call_back回调函数
                elif event.key==pygame.K_s:
                    s_down_cb()
                elif event.key==pygame.K_a:
                    a_down_cb()
                elif event.key==pygame.K_d:
                    d_down_cb()
    pygame.quit()


if __name__ == "__main__":
    main()