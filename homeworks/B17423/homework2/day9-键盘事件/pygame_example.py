# -*- coding: utf-8 -*-
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode([640, 480])
    running  = True
    while running:
        screen.fill([255,255,255]) # R G B white
        pygame.draw.circle(screen, [255, 0, 0], [100, 100], 10, 0) #最后一个参数是默认参数 默认参数为0
        pygame.draw.rect(screen, [0, 255, 255], [280, 400, 80, 5], 0) #最后一个参数是默认参数 默认参数为0
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == '__main__':
    main()
