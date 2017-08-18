# -*- coding: utf-8 -*-
import pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode([640,480]) #分辨率 返回screen操作变量
    running = True
    while running:
        screen.fill([255,255,255])
        pygame.draw.circle(screen, [255,0,0], [100,100], 10, 0) #0球 1圆环
        pygame.draw.rect(screen, [0,255,255],[280,400,80,5],0) #0实心 1或其他边框厚度
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
if __name__ == '__main__':
	main()