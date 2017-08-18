# -*- coding: utf-8 -*-
import pygame,random

SCALE = 20  #地图中有多少格
SIZE = 20   #每一格的大小
WIDTH = SCALE * SIZE
HEIGHT = SCALE * SIZE

DIRECT = [[0,-1],[-1,0],[0,1],[1,0]] #上左下右
dirt = 1 #蛇前进的方向  往左
#dirt = 0 #蛇前进的方向  往上


snake = [[4,3],[5,3],[6,3]]
apple = [random.randint(0, WIDTH / SIZE),random.randint(0, HEIGHT / SIZE)]


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
    if new_body == apple:
        snake.insert(0, new_body)
    else:
        snake.insert(0, new_body)
        snake.pop()

def apple_update():
    global dirt
    if apple == snake[0]:  #如果蛇吃到苹果，生成新的苹果
        apple[0] = random.randint(0, WIDTH / SIZE)
        apple[1] = random.randint(0, HEIGHT / SIZE)

def game_over(screen):
    pygame.font.init()
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont("arial", 50)
    warning = font.render("Game Over!", True, (255, 0, 0))
    screen.blit(warning, (WIDTH / 4, HEIGHT / 2))
    pygame.time.wait(100)
    pygame.display.update()


def snake_death(screen):
    if (snake[0] in snake[1:]) or (snake[0][0] <= 0) or (snake[0][0] >= WIDTH) or (snake[0][1] <= 0) or (snake[0][1] >= HEIGHT):
        game_over(screen)

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
    running  = True

    while running:
        pygame.time.delay(200) # 50ms
        snake_update()
        apple_update()
        screen_show(screen)
        snake_death(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and dirt != 2 :
                    w_down_cb()
                elif event.key == pygame.K_s and dirt != 0:
                    s_down_cb()
                elif event.key == pygame.K_a and dirt != 3:
                    a_down_cb()
                elif event.key == pygame.K_d and dirt != 1:
                    d_down_cb()

    pygame.quit()

if __name__ == '__main__':
    main()
