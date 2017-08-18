# -*- coding: utf-8 -*-
import pygame
import random

SCALE = 20  
SIZE = 20   
WIDTH = SCALE * SIZE
HEIGHT = SCALE * SIZE

DIRECT = [[0,-1],[-1,0],[0,1],[1,0]]
dirt = 1 

snake = [[4,3],[5,3],[6,3]]
apple = [10,2]

def screen_show(screen):
    screen.fill([255,255,255])
    for body in snake:
        pygame.draw.rect(screen, [0, 255,0], [body[0]*SIZE,body[1]*SIZE, SIZE - 1, SIZE - 1])
    pygame.draw.circle(screen, [255, 0, 0], [apple[0]*SIZE + SIZE / 2, apple[1]*SIZE + SIZE / 2], SIZE/2)
    pygame.display.flip()

def lose():
    screen.fill([255,255,255])
    font = pygame.font.Font(None, 100)
    text = font.render("GAME OVER",True, [255,0,0])
    screen.blit(text, [0,100])
    img = pygame.image.load("beach_ball.png")
    screen.blit(img, [0, 0])    
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

def eat():
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

    while running:
        pygame.time.delay(200) # 200ms
        if snake_update():
            new_apple()

        if eat():
            lose()

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
