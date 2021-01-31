# -*- coding: utf-8 -*-
import pygame
import random
from pygame.locals import *

SCALE = 20  #地图中有多少格
SIZE = 20   #每一格的大小
WIDTH = SCALE * SIZE
HEIGHT = SCALE * SIZE
lose=False

DIRECT = [[0,-1],[-1,0],[0,1],[1,0]]
dirt = 1 #蛇前进的方向

snake = [[4,3],[5,3],[6,3]]
apple = [3,1]

def screen_show(screen,lose):
    screen.fill([255,255,255])
    for body in snake:
        pygame.draw.rect(screen, [0, 255,0], [body[0]*SIZE,body[1]*SIZE, SIZE - 1, SIZE - 1])
    pygame.draw.rect(screen, [0, 0,255], [snake[0][0] * SIZE, snake[0][1] * SIZE, SIZE - 1, SIZE - 1])
    img = pygame.image.load("beach_ball.png")
    screen.blit(img, [apple[0]*SIZE, apple[1]*SIZE])
    # pygame.draw.circle(screen, [255, 0, 0], [apple[0]*SIZE + SIZE / 2, apple[1]*SIZE + SIZE / 2], SIZE/2)
    if lose:
        font = pygame.font.Font(None, 50)
        text = font.render("YOU LOSE", True, [255, 0, 0])
        screen.blit(text, [120, 60])
        font = pygame.font.Font(None, 30)
        text = font.render("press mouse restart", True, [255, 0, 0])
        screen.blit(text, [110, 120])
    pygame.display.flip()

def snake_update():
    global dirt
    new_body = [0,0]
    new_body[0] = (snake[0][0] + DIRECT[dirt][0]) % SCALE
    new_body[1] = (snake[0][1] + DIRECT[dirt][1]) % SCALE
    if new_body == apple:
        snake.insert(0, new_body)
        return True
    else:
        snake.insert(0, new_body)
        snake.pop()
        return False

def is_lose():
    if snake.count(snake[0]) >= 2:

        return True
    return False

def new_apple():
    apple[0] = random.randint(0,19)
    apple[1] = random.randint(0,19)

def w_down_cb():
    global dirt
    if dirt % 2 !=0:
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
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    running  = True
    EX=True
    while EX:
        while running:
            global lose
            pygame.time.delay(200) # 200ms
            if snake_update():
                new_apple()

            if is_lose():
                lose=True
                running=False
                break

            screen_show(screen,lose)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    EX=False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        w_down_cb()
                    elif event.key == pygame.K_s:
                        s_down_cb()
                    elif event.key == pygame.K_a:
                        a_down_cb()
                    elif event.key == pygame.K_d:
                        d_down_cb()
        screen_show(screen ,lose)
        global snake,apple
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                running = True
                EX = True
                lose=False
                snake = [[4, 3], [5, 3], [6, 3]]
                apple = [3, 1]
            if event.type == pygame.QUIT:
                EX = False
    #YOU LOSE
    pygame.quit()

if __name__ == '__main__':
    main()
