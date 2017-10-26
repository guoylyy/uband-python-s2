# -*- coding: utf-8 -*-

import pygame
import random

SCALE = 20#地图中有多少格，把整个的screen分成20*20格的地图
SIZE = 30#每一格的大小
WIDTH = SCALE * SIZE
HEIGHT = SCALE * SIZE
DIRECT = [[0,-1],[-1,0],[0,1],[1,0]]
dirt = 1#蛇前进的方向，即往左


snake = [[4,3],[5,3],[6,3]]
apple = [3,1]

def screen_show(screen):
	screen.fill([255,255,255])
	for body in snake:
		pygame.draw.rect(screen,[0,255,0],[body[0]*SIZE,body[1]*SIZE, SIZE - 1, SIZE - 1])#-1是为了看到每个格子之间有分线，不是连成一体的
	pygame.draw.circle(screen,[255,0,0],[apple[0]*SIZE + SIZE/2, apple[1]*SIZE + SIZE/2], SIZE/2)
	pygame.display.flip()

def snake_update():
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

def is_lose():
    if snake.count(snake[0]) >= 2:#如果蛇头在蛇的身体里有两份，就说明碰到自己的身体了
        return True
    return False#else:return False,这里省略了

def lose_show(screen):
    screen.fill([255,255,255])
    font = pygame.font.Font(None, 80)#字体None=默认字体，字号
    text = font.render("YOU LOSE THE GAME", True, [255,0,0])# render(text, antialias, color, background=None)
    screen.blit(text, [0,200])#显示对象 位置
    img = pygame.image.load("tanchishe.png")#图片路径，一般和python源文件放在一个目录下
    screen.blit(img, [0, 0])    
    pygame.display.flip()

def new_apple():
    apple[0] = random.randint(0,19)#randint代表0到19取一个随机值，包括0和19
    apple[1] = random.randint(0,19)

def w_down_cb():#往上走的，按w或s都不应该有反应
    global dirt
    if dirt % 2 != 0:#只有在左右行走的时候，按w才有往上走的功能
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
    screen = pygame.display.set_mode([WIDTH,HEIGHT])
    running = True

    while running:
        pygame.time.delay(200)#50ms，不然画面闪的很快
        if snake_update():
            new_apple()

        if is_lose():
            lose_show(screen)
            running = False
            # break#如果吃到自己，程序退出
        screen_show(screen)
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
    
    while running == False:
        lose_show(screen)
    # pygame.time.delay(1000000)
        for event in pygame.event.get():
            while event.type == pygame.QUIT:
                pygame.quit()

if __name__ == '__main__':
    main()