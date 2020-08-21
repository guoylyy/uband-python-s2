#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: lina 20170909

import pygame
import random

SCALE = 20
SIZE = 20
WIDTH = SCALE * SIZE
HIGHT = SCALE * SIZE

DIRECT = [[0,-1],[-1,0],[0,1],[1,0]]
dirt = 1

snake = [[4,3],[5,3],[6,3]]
apple = [3,1]

def screen_show(screen):
    screen.fill([0,0,0])
    for body in snake:
        pygame.draw.rect(screen,[0,100,255],[body[0]*SIZE,body[1]*SIZE,SIZE-1,SIZE-1],0)
    pygame.draw.circle(screen,[255,0,0],[apple[0]*SIZE+SIZE/2,apple[1]*SIZE+SIZE/2],SIZE/2,0)
    pygame.display.flip()

def snake_update():
    global dirt
    new_body = [0,0]
    new_body[0] = (snake[0][0] + DIRECT[dirt][0]) % SCALE
    new_body[1] = (snake[0][1] + DIRECT[dirt][1]) % SCALE
    if new_body == apple:
        snake.insert(0,new_body)
        return True
    else:
        snake.insert(0,new_body)
        snake.pop()
        return False

def new_apple():
    apple[0] = random.randint(0,19)
    apple[1] = random.randint(0,19)

def is_lose():
    if snake.count(snake[0]) >= 2:
        return True
    else:
        return False


def w_down_cb():
    global dirt
    if dirt % 2 != 0:
        dirt = 0

def s_down_cb():
    global dirt
    if dirt % 2 != 0:
        dirt = 2

def a_down_cb():
    global dirt
    if dirt % 2 != 1:
        dirt = 1

def d_down_cb():
    global dirt
    if dirt % 2 != 1:
        dirt = 3

def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH,HIGHT])
    pygame.display.set_caption("Hello, snake!")
    running = True

    while running:
        pygame.time.delay(200) #ms
        if snake_update():
            new_apple()
        if is_lose():
            break
        screen_show(screen)

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