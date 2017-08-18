# -*- coding: utf-8 -*-
import pygame
import random

SCALE = 20  #地图中有多少格
SIZE = 20   #每一格的大小
WIDTH = SCALE * SIZE
HEIGHT = SCALE * SIZE

snake = [[17,3],[18,3],[19,3]]
speed = [-1, 0]
apple = [3,1]

def end_or_not():
    running = True
    if snake.count(snake[0]) >= 2:#判断时候咬到身体
        running = False
    n = 0
    for body in snake:
        if body[0] < 0 or body[0] >= SCALE or body[1] < 0 or body[1] >= SCALE:
            running = False
            # pygame.quit()
        n += 1
    return running


def update_snake():
    new_snake_head = [0,0]
    new_snake_head[0] = (snake[0][0] + speed[0])
    new_snake_head[1] = (snake[0][1] + speed[1])
    snake.insert(0, new_snake_head)
    if new_snake_head != apple:
        snake.pop()
    else :
        apple[0] = random.randint(0,19)
        apple[1] = random.randint(0,19)

def screen_show(screen):
    screen.fill([255,255,255])
    n = 0
    for body in snake:
        if n == 0:
            pygame.draw.rect(screen, [0, 0, 255], [body[0] * SIZE, body[1] * SIZE, SIZE - 1, SIZE - 1])
        else:
            pygame.draw.rect(screen, [0, 255, 0], [body[0] * SIZE, body[1] * SIZE, SIZE - 1, SIZE - 1])
        n += 1
    pygame.draw.circle(screen, [255, 0, 0], [apple[0]*SIZE + SIZE / 2, apple[1]*SIZE + SIZE / 2], SIZE/2)
    pygame.display.flip()

def w_down_cb():
    global speed
    if speed[0] != 0:
        speed = [0, -1]

def s_down_cb():
    global speed
    if speed[0] != 0:
        speed = [0, 1]

def a_down_cb():
    global speed
    if speed[1] != 0:
        speed = [-1, 0]

def d_down_cb():
    global speed
    if speed[1] != 0:
        speed = [1, 0]

# def screen_show(screen):
#     screen.fill([255,255,255])
#     font = pygame.font.Font(None, 100)
#     text = font.render("game over", True, [255,0,0])
#     screen.blit(text, [0,100])
#     # img = pygame.image.load("beach_ball.png")
#     # screen.blit(img, [0, 0])
#     pygame.display.flip()

def main():

    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    running  = True
    if not running:
        screen_show(screen)
    while running:
        pygame.time.delay(200) # 50ms
        screen_show(screen)
        update_snake()
        running = end_or_not()
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