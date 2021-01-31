# -*- coding: utf-8 -*-
import pygame
import random

SCALE = 20  #地图中有多少格
SIZE = 20   #每一格的大小
WIDTH = SCALE * SIZE
HEIGHT = SCALE * SIZE

DIRECT = [[0,-1],[-1,0],[0,1],[1,0]]
dirt = 1 #蛇前进的方向
dirt_old = 1

snake = [[4,3],[5,3],[6,3]]
apple = [3,1]

def screen_show(screen):
    screen.fill([255,255,255])

    # lose_show(screen)

    for index,body in enumerate(snake):
        if index == 0:
            pygame.draw.rect(screen, [0, 100, 0], [body[0] * SIZE, body[1] * SIZE, SIZE - 1, SIZE - 1])
        else:
            pygame.draw.rect(screen, [0, 255,0], [body[0]*SIZE,body[1]*SIZE, SIZE - 1, SIZE - 1])
    # for body in snake:
    #     pygame.draw.rect(screen, [0, 255,0], [body[0]*SIZE,body[1]*SIZE, SIZE - 1, SIZE - 1])
    # pygame.draw.circle(screen, [255, 0, 0], [apple[0]*SIZE + SIZE / 2, apple[1]*SIZE + SIZE / 2], SIZE/2)
    img = pygame.image.load("beach_ball.png")
    img = pygame.transform.scale(img,(SIZE,SIZE))
    screen.blit(img, [apple[0]*SIZE, apple[1]*SIZE])
    pygame.display.flip()

def lose_show(screen):
    screen.fill([255,255,255])
    font = pygame.font.Font(None, 100)
    text = font.render("Game Over", True, [255,0,0])
    screen.blit(text, [0,100])
    pygame.display.flip()

def snake_update():
    global dirt
    global dirt_old
    if dirt_old - dirt == 2 or dirt_old - dirt == -2:   #禁止掉头
        dirt = dirt_old
    new_body = [0,0]
    new_body[0] = (snake[0][0] + DIRECT[dirt][0]) % SCALE
    new_body[1] = (snake[0][1] + DIRECT[dirt][1]) % SCALE
    if new_body == apple:
        snake.insert(0, new_body)
    else:
        snake.insert(0, new_body)
        snake.pop()

    dirt_old = dirt

def snake_if_die():
    for num in range(1,len(snake)):
        if snake[0] == snake[num]:
            return True
    return False

def snake_if_eat():
    if snake[0] == apple:
        return True

def apple_update():
    if snake_if_eat():
        apple[0] = random.randint(0,19)
        apple[1] = random.randint(0,19)

def w_down_cb():
    global dirt
    dirt = 0

def s_down_cb():
    global dirt
    dirt = 2

def a_down_cb():
    global dirt
    dirt = 1

def d_down_cb():
    global dirt
    dirt = 3

def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    running = True

    while running:
        pygame.time.delay(200)  # 50ms
        snake_update()
        apple_update()
        screen_show(screen)

        if snake_if_die():
            lose_show(screen)
            running = False

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
