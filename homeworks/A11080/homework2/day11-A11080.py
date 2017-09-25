#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: lina 20170906

import pygame

MOU_CON = True

board = pygame.Rect(280,400,80,5)
circle = [100,100]
RADIUS = 10
SPEED = [5,-5]
WIDTH = 640
HIGHT = 480

def renew_ball():
    if circle[1] > HIGHT:
        circle[0] = 100
        circle[1] = 100

def draw_surface(screen):
    screen.fill([0, 0, 0])
    pygame.draw.circle(screen, [255, 0, 0], circle, RADIUS, 0)
    pygame.draw.rect(screen, [255, 255, 0], board)
    pygame.display.flip()

def update_ball():
    circle[0] += SPEED[0]
    circle[1] += SPEED[1]

    if circle[1]-RADIUS == 0:
        SPEED[1] *= -1
    if circle[0]+RADIUS == WIDTH or circle[0]-RADIUS == 0:
        SPEED[0] *= -1
    if (circle[0] >= (board.centerx - 40)) and (circle[0] <= (board.centerx + 40)) and (circle[1]+RADIUS == 400):
    # if circle[0] > board.left and circle[0] < board.right and (circle[1]+RADIUS == board.top)
        SPEED[1] *= -1

def update_board():
    (x,y) = pygame.mouse.get_pos()
    board.centerx = x
    # board.centery = y

def w_down_cb():
    if not MOU_CON:
        board.centery -= 5

def s_down_cb():
    if not MOU_CON:
        board.centery += 5

def a_down_cb():
    if not MOU_CON:
        board.centerx -= 8

def d_down_cb():
    if not MOU_CON:
        board.centerx += 8

def main():
    pygame.init()
    screen = pygame.display.set_mode([640,480])
    running = True

    while running:
        pygame.time.delay(50) #ms
        update_board()
        update_ball()
        renew_ball()
        draw_surface(screen)
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