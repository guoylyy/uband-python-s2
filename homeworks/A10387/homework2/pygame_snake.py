# -*- coding: utf-8 -*-
import pygame
import random

SCALE = 20  #地图中有多少格
SIZE = 20   #每一格的大小
WIDTH = SCALE * SIZE
HEIGHT = SCALE * SIZE

DIRECT = [[0,-1],[-1,0],[0,1],[1,0]]
dirt = 1 #初始化蛇前进的方向

snake = [[4,3],[5,3],[6,3]]
appleCoord = [3,1]
apple = pygame.image.load("apple.png")
score = 0

def screen_show(screen):
    screen.fill([255,255,255])
    for body in snake:
        pygame.draw.rect(screen, [0, 255,0], [body[0]*SIZE,body[1]*SIZE, SIZE - 1, SIZE - 1])
        screen.blit(apple, [appleCoord[0]*SIZE, appleCoord[1]*SIZE])
    pygame.display.flip()

    if snake.count(snake[0]) >= 2:
        game_over(score, screen)

def snake_update():
    global dirt
    global appleCoord
    global screen
    new_body = [0,0]
    new_body[0] = (snake[0][0] + DIRECT[dirt][0]) % SCALE
    new_body[1] = (snake[0][1] + DIRECT[dirt][1]) % SCALE
    if new_body == appleCoord:
        snake.insert(0, new_body)
        appleCoord = [int(random.random()*20), int(random.random()*20)]
    else:
        snake.insert(0, new_body)
        snake.pop()
    
        

def game_over(score, screen):
    my_font = pygame.font.SysFont(None, 50)
    levelstr = 'GAME OVER'
    text = my_font.render(levelstr, True, (255, 0, 0))
     
    textRect = text.get_rect()  
    textRect.centerx = screen.get_rect().centerx  
    textRect.centery = screen.get_rect().centery   
    screen.blit(text,textRect)  

    my_font2 = pygame.font.SysFont(None, 16)
    nextstr = 'Click on r if you want to continue!!!'
    text2 = my_font2.render(nextstr, True, (0,0,255))

    textRect2 = text.get_rect()
    textRect2.centerx = screen.get_rect().centerx
    textRect2.centery = screen.get_rect().centery+40
    screen.blit(text2,textRect2)

    # keydown r restart,keydown n exit  
    while 1:  
        event = pygame.event.poll()  
        if event.type == pygame.QUIT:  
            pygame.quit()  
            exit(0)  
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_r:  
                restart = True  
                snake = [[4,3],[5,3],[6,3]]
                apple = [3,1]
                break  
            if event.key == pygame.K_n:  
                restart = False  
                break  
        pygame.display.update()  


def w_down_cb():
    global dirt
    if dirt != 2:
        dirt = 0

def s_down_cb():
    global dirt
    if dirt != 0:
        dirt = 2

def a_down_cb():
    global dirt
    if dirt != 3:
        dirt = 1

def d_down_cb():
    global dirt
    if dirt != 1:
        dirt = 3

def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    running  = True

    while running:
        pygame.time.delay(200) # 50ms
        snake_update()
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
