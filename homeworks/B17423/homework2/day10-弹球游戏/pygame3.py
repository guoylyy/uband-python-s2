# -*- coding: utf-8 -*-
import pygame

MOU_CON = False

board = pygame.Rect(280, 400, 80, 5)
#board是rect类的一个实例对象
#board的上边缘：board.top
#board的左边缘：board.left
#board的右边缘：board.right
circle = [100, 100]
RADIUS = 10
SPEED = [5, -5]
WIDTH = 640
HEIGHT = 480


def update_ball():
    if circle[1] - RADIUS == 0 or circle[1] + RADIUS == HEIGHT:   #到上边缘或下边缘
        SPEED[1] *= -1
    if circle[0] + RADIUS == WIDTH or circle[0] - RADIUS == 0:     #右边缘或左边缘
        SPEED[0] *= -1

    if (circle[1] + RADIUS == board.top or circle[1] - RADIUS == board.bottom) and circle[0] in range(board.left, board.right):  #碰到板子
        SPEED[1] *= -1
    if (circle[0] + RADIUS == board.left or circle[0] - RADIUS == board.right) and circle[1] in range(board.top, board.bottom):
        SPEED[0] *= -1

    circle[0] += SPEED[0]
    circle[1] += SPEED[1]


def draw_surface(screen):
    screen.fill([255, 255, 255])  # R G B white
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
    running = True

    while running:
        pygame.time.delay(50)  # 50ms
        update_board()
        update_ball()
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
