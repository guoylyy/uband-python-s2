# -*- coding: utf-8 -*-

import pygame

SCALE = 20#地图中有多少格，把整个的screen分成20*20格的地图
SIZE = 20#每一格的大小
WIDTH = SCALE * SIZE
HEIGHT = SCALE * SIZE

head = [4,3]
snake = [[5,3],[6,3]]
apple = [3,1]

def screen_show(screen):
	screen.fill([255,255,255])
	pygame.draw.rect(screen,[0,255,0],[head[0]*SIZE,head[1]*SIZE,SIZE - 1,SIZE - 1])
	pygame.draw.circle(screen,[255,0,0],[head[0]*SIZE + SIZE/2,head[1]*SIZE + SIZE/2],2)
	for body in snake:
		pygame.draw.rect(screen,[0,255,0],[body[0]*SIZE,body[1]*SIZE,SIZE - 1,SIZE - 1])#-1是为了看到每个格子之间有分线，不是连成一体的
	pygame.draw.circle(screen,[255,0,0],[apple[0]*SIZE + SIZE/2,apple[1]*SIZE + SIZE/2],SIZE/2)
	pygame.display.flip()

def w_down_cb():
    pass

def s_down_cb():
    pass

def a_down_cb():
    pass

def d_down_cb():
    pass

def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH,HEIGHT])
    running = True

    while running:
        pygame.time.delay(50)#50ms，不然画面闪的很快
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
    pygame.quit()

if __name__ == '__main__':
    main()