# -*- coding: utf-8 -*-
import pygame

MOU_CON = True

board = pygame.Rect(280, 400, 80, 5)
circle = [100, 100]
RADIUS = 10
SPEED = [5, -5]
WIDTH = 640
HEIGHT = 480


def renew_ball():
    if circle[1] > HEIGHT:
        circle[0] = 100
        circle[1] = 100

def update_ball():
    #zuo
    if circle[1] - RADIUS == 0:
        SPEED[1] *= -1

    #right&top
    if circle[0] + RADIUS == WIDTH or circle[0] - RADIUS == 0:
        SPEED[0] *= -1

    #board
    if circle[1] + RADIUS == board.top and circle[0] > board.left and circle[0] < board.right:
        SPEED[1] *= -1

    circle[0] += SPEED[0]
    circle[1] += SPEED[1]


def draw_surface(screen):
    screen.fill([255, 255, 255])  #white
    pygame.draw.circle(screen, [255, 0, 0], circle, RADIUS)
    pygame.draw.rect(screen, [0, 255, 255], board)
    pygame.display.flip()

def update_board():
    if MOU_CON:
        (x, y) = pygame.mouse.get_pos()
        board.centerx = x


def w_down_cb():
    pass

def s_down_cb():
    pass

def a_down_cb():
    if not MOU_CON:
        board.centerx -= 5

def d_down_cb():
    if not MOU_CON:
        board.centerx += 5

def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    running  = True

    while running:
        pygame.time.delay(50) # 50ms
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
