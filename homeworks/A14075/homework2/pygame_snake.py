# -*- coding: utf-8 -*-
import pygame
import random

SCALE = 20  #地图中有多少格
SIZE = 20   #每一格的大小
WIDTH = SCALE * SIZE
HEIGHT = SCALE *SIZE + SCALE
DIRECT = [[0,-1],[-1,0],[0,1],[1,0]]    #上左下右
dirt = 1

def move(snake,apple,score):
    new_body = [0,0]
    new_body[0] = (snake[0][0] + DIRECT[dirt][0]) % 20
    new_body[1] = (snake[0][1] + DIRECT[dirt][1]) % 20
    if new_body in snake:
        return False,score
    else:
        snake.insert(0, new_body)
    if new_body == apple:
        update_apple(apple,snake)
        score += 1
    else:
        snake.pop()
    return True,score

def screen_show(screen,snake,apple,score,Mscore):
    screen.fill([255,255,255])
    for index,body in enumerate(snake):
        if index == 0 :
            pygame.draw.rect(screen, [0, 0, 255], [body[0] * SIZE, body[1] * SIZE, SIZE - 1, SIZE - 1])
        else:
            pygame.draw.rect(screen, [0, 255,0], [body[0]*SIZE,body[1]*SIZE, SIZE - 1, SIZE - 1])
    pygame.draw.circle(screen, [255, 0, 0], [int(apple[0]*SIZE + SIZE / 2), int(apple[1]*SIZE + SIZE / 2)], int(SIZE/2))
    font = pygame.font.Font(None, SCALE)  # Font(filename,size)
    text1 = font.render('Your score:' + str(score), True, [0, 0, 0])
    text2 = font.render('Highest score:' + str(Mscore), True, [0, 0, 0])
    screen.blit(text1 , [0, HEIGHT-SCALE])
    screen.blit(text2 , [WIDTH/2, HEIGHT-SCALE])
    pygame.display.flip()

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

def update_apple(apple,snake):
    apple[0] = random.randint(0, SCALE-1)
    apple[1] = random.randint(0, SCALE-1)
    if apple in snake:
        update_apple(apple,snake)

def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    running = True
    Mscore = 0
    score = 0
    while running:
        if (Mscore<score):
            Mscore = score
        alive = True
        score = 0
        snake = [[4, 3], [5, 3], [6, 3]]
        apple = [3, 1]
        while alive:
            pygame.time.delay(50)
            screen_show(screen, snake, apple,score,Mscore)
            alive,score = move(snake,apple,score)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    alive = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        w_down_cb()
                    elif event.key == pygame.K_s:
                        s_down_cb()
                    elif event.key == pygame.K_a:
                        a_down_cb()
                    elif event.key == pygame.K_d:
                        d_down_cb()

if __name__ == '__main__':
    main()
