# -*- coding: UTF-8 -*-


import pygame
import random


SCALE = 20    #20*20的图  地图中有多少格
SIZE = 20     #每一格的大小
WIDTH = SCALE * SIZE
HEIGHT = SCALE * SIZE

DIRECT = [[0, -1], [-1, 0], [0, 1], [1, 0]]   # UP FORWARD DOWN BACKWARD
dirt = 1  #初始化方向   方向相当于是上面数组的下标  

snake = [[4, 3], [5, 3], [6, 3]]
apple = [3, 1]

def screen_show(screen):
    screen.fill([255, 255, 255])
    for body in snake:
        pygame.draw.rect(screen, [0, 0, 0], [snake[0][0] * SIZE, snake[0][1] * SIZE, SIZE - 1, SIZE - 1])
        #蛇头的颜色换一下
        pygame.draw.rect(screen, [0, 255, 0], [body[0] * SIZE, body[1] * SIZE, SIZE - 1, SIZE - 1])
        # size-1的原因是这样身体之间会有个间隙
    pygame.draw.circle(screen, [255, 0, 0], [apple[0] * SIZE + SIZE / 2, apple [1] * SIZE + SIZE / 2], SIZE / 2)
     #圆心的位置要先确认左上角*一个格子的大小，再加上格子长度的一般。
    
    pygame.display.flip() 


def snake_update():
    new_body = [0, 0]
    new_body[0] = (snake[0][0] + DIRECT[dirt][0]) % SCALE #snake[0] 是蛇头 
    new_body[1] = (snake[0][1] + DIRECT[dirt][1]) % SCALE
    
    if new_body == apple:
        snake.insert(0, new_body)    #注意是圆括号
        return True

    else:
        snake.insert(0, new_body)
        snake.pop()
        return False

def new_apple():   #生成新苹果  但是蛇什么时候吃到苹果要取决于蛇
    apple[0] = random.randint(0, 19) #随机生成一个包括0，包括19的数字
    apple[1] = random.randint(0, 19)

def fail():    #蛇要是吃到自己就输掉  头在身体里面
    if snake.count(snake[0]) >= 2:
        return True
    return False

# 在按键回调函数中判断，
# 如果当前蛇和回调函数需要设置的方向为同向或反向，则不必更新蛇运行的方向
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
        pygame.time.delay(200)   #50是毫秒

        if snake_update():
            new_apple()
       
        if fail():
            break

        screen_show(screen)  #这个都是放在动作的最后的


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    w_down_cb()    #回调函数 call back
                elif event.key == pygame.K_s:
                    s_down_cb()
                elif event.key == pygame.K_a:
                    a_down_cb()
                elif event.key == pygame.K_d:
                    d_down_cb()

    font = pygame.font.Font(None, 50)
    text = font.render("Failed", True, [255,0,0])
    screen.blit(text, [40, 60])
    # img = pygame.image.load("beach_ball.png")
    # screen.blit(img, [0, 0])   
    pygame.display.flip() 
    

    pygame.quit()  

if __name__ == '__main__':
    main()
     