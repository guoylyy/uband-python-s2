#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Liluo

import pygame

def main():
    pygame.init()
    screen=pygame.display.set_mode([640,490]) #生成游戏界面大小
    running = True
    while running:
        screen.fill([255,255,255]) #RGB
        pygame.draw.circle(screen,[255,0,0],[100,100],10,0)  #0-圆球 实心，1-圆环
        pygame.draw.rect(screen,[0,255,255],[280,400,80,5],0) #rectangle, 左上角坐标
        pygame.draw.polygon(screen,[100,150,200],[[200,0],[100,300],[0,0]],1)# ，宽度高度
        pygame.draw.ellipse(screen, [0, 0, 0], [370, 400, 80, 20], 0)
        pygame.draw.line(screen, [0, 255, 0], [0, 0], [50, 30], 5)

        # Draw on the screen a GREEN line from (0,0) to (50.75)
        # 5 pixels wide.
        pygame.draw.lines(screen, [0, 0, 0], False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)
        pygame.display.flip()#写在screen上的东西显示

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running =False
    pygame.quit()

if __name__ == "__main__":
    main()