# -*- coding: utf-8 -*-
import pygame
import random

SCALE = 20  #地图中有多少格
SIZE = 20   #每一格的大小
WIDTH = SCALE * SIZE
HEIGHT = SCALE * SIZE

snake = [[4, 3], [5, 3], [6, 3], [7, 3]]
apple = [3, 1]

direct = [[0, -1], [-1, 0], [0, 1], [1, 0]]  #向上，向左，向下，向右
k = 0

def show_error(screen):
    screen.fill([255, 255, 255])  # white
    font = pygame.font.Font(None, 50)
    text = font.render("GAME OVER", True, [255, 0, 0])
    screen.blit(text, [120, 120])
    img = pygame.image.load("beach_ball.png")
    screen.blit(img, [0, 0])
    pygame.display.flip()


def screen_show(screen):
    screen.fill([255, 255, 255])   #white
    font = pygame.font.Font(None, 20)
    text = font.render("Retro Snake", True, [255, 0, 0])
    screen.blit(text, [300, 0])
    head = snake[0]
    pygame.draw.circle(screen, [0, 255, 0], [head[0] * SIZE + SIZE // 2, head[1] * SIZE + SIZE // 2], SIZE // 2)  #head
    for body in snake[1:]:
        pygame.draw.rect(screen, [0, 255, 0], [body[0]*SIZE, body[1]*SIZE, SIZE - 1, SIZE - 1])    #snake
    pygame.draw.circle(screen, [255, 0, 0], [apple[0]*SIZE + SIZE // 2, apple[1]*SIZE + SIZE // 2], SIZE // 2)   #apple
    pygame.display.flip()


def update_snake():
    global k
    head = snake[0]
    new_head = [0, 0]
    new_head[0] = (head[0] + direct[k][0]) % SCALE  #超过屏幕再回到另一端
    new_head[1] = (head[1] + direct[k][1]) % SCALE
    if new_head not in snake:             #没撞到自己
        snake.insert(0, new_head)
        if new_head == apple:     #吃到苹果,增长一截
            apple[0] = random.randint(0, 19)
            apple[1] = random.randint(0, 19)
        else:
            snake.pop()  #没吃到苹果，去掉尾巴
        return True

    else:
        return False

def w_down_cb():
    global k
    if k % 2 == 1:   #当前蛇向左或向右
        k = 0

def s_down_cb():
    global k
    if k % 2 == 1:  # 当前蛇向左或向右
        k = 2

def a_down_cb():
    global k
    if k % 2 == 0:  # 当前蛇向上或向下
        k = 1

def d_down_cb():
    global k
    if k % 2 == 0:  # 当前蛇向上或向下
        k = 3

def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    running = True

    while running:
        pygame.time.delay(200)  # 200ms
        suc = update_snake()
        if not suc:
            show_error(screen)
            pygame.time.delay(3000)  # 200ms
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
    #show_error(screen)
    pygame.quit()

if __name__ == '__main__':
    main()
