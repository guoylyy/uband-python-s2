# -*- coding: utf-8 -*-
import pygame
import random

SCALE = 20  #地图中有多少格
SIZE = 20   #每一格的大小
WIDTH = SCALE * SIZE
HEIGHT = SCALE * SIZE

DIRECT = [[0,-1],[-1,0],[0,1],[1,0]]
dirt = 1 #蛇前进的方向



snake = [[4,3],[5,3],[6,3]]
apple = [3,1]

def screen_show(screen):
    screen.fill([255,255,255])
    for body in snake:
        pygame.draw.rect(screen, [0, 255,0], [body[0]*SIZE,body[1]*SIZE, SIZE - 1, SIZE - 1])
    pygame.draw.circle(screen, [255, 0, 0], [apple[0]*SIZE + SIZE / 2, apple[1]*SIZE + SIZE / 2], SIZE/2)
    pygame.display.flip()

def snake_update():
    global dirt
    new_body = [0,0]
    new_body[0] = (snake[0][0] + DIRECT[dirt][0]) % SCALE
    new_body[1] = (snake[0][1] + DIRECT[dirt][1]) % SCALE
    snake.insert(0, new_body)
    if new_body != apple:
        snake.pop()
        return False
    return True

def apple_update():
    apple[0] = random.randint(1, 20)
    apple[1] = random.randint(1, 20)
        

def is_fail():   
    if snake.count(snake[0]) >= 2:
        return True
        #只要判断蛇头有没有和蛇身重叠，不用判断全部

def fail_show(screen): #失败显示lose
    screen.fill([255,255,255])
    font = pygame.font.Font(None, 100)   #字体None=默认字体，字号 
    text = font.render("YOU LOSE", False, [255,0,0]) # render(text, antialias, color, background=None)  antialias 消除字体不平滑度
    screen.blit(text, [0,100]) #显示对象 位置
    pygame.display.flip()

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
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    running = True

    while running:
        pygame.time.delay(200) 
        if snake_update():
            apple_update()
        screen_show(screen)
        if is_fail():
            break
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
    fail_show(screen)
    pygame.quit()

if __name__ == '__main__':
    main()