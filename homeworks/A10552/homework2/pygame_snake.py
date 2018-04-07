# -*- coding: utf-8 -*-
import pygame
import random

SCALE = 20  # 地图中有多少格
SIZE = 20  # 每一格的大小
WIDTH = SCALE * SIZE
HEIGHT = SCALE * SIZE
DIRECT = [[0, -1], [-1, 0], [0, 1], [1, 0]]
direct = 1  # 蛇前进的方向

snake = [[4, 3], [5, 3], [6, 3]]
apple = [3, 1]


def screen_show(screen):
	screen.fill([255, 255, 255])
	pygame.draw.rect(screen, [255, 255, 0], [snake[0][0] * SIZE, snake[0][1] * SIZE, SIZE - 1, SIZE - 1])
	for body in snake[1:]:
		pygame.draw.rect(screen, [0, 255, 0], [body[0] * SIZE, body[1] * SIZE, SIZE - 1, SIZE - 1])
	pygame.draw.circle(screen, [255, 0, 0], [apple[0] * SIZE + SIZE / 2, apple[1] * SIZE + SIZE / 2], SIZE / 2)
	pygame.display.flip()


def gameover_show(screen):
	font = pygame.font.Font(None, 100)
	text = font.render("Game Over", True, [255, 0, 0])
	screen.blit(text, [0, 100])
	pygame.display.flip()


def generate_apple():
	while True:
		apple[0] = random.randint(0, 19)
		apple[1] = random.randint(0, 19)
		if apple not in snake:
			break


def is_lose():
	if snake[0][0] < 0 or snake[0][0] > SCALE - 1 or snake[0][1] < 0\
			or snake[0][1] > SCALE - 1 or snake.count(snake[0]) > 1:
		return True
	return False


def move_snake():
	global direct

	next_pos = [0, 0]
	next_pos[0] = snake[0][0] + DIRECT[direct][0]
	next_pos[1] = snake[0][1] + DIRECT[direct][1]

	snake.insert(0, next_pos)
	if next_pos == apple:
		generate_apple()
	else:
		snake.pop()


def w_down_cb():
	global direct
	if direct % 2 != 0:
		direct = 0


def a_down_cb():
	global direct
	if direct % 2 != 1:
		direct = 1


def s_down_cb():
	global direct
	if direct % 2 != 0:
		direct = 2


def d_down_cb():
	global direct
	if direct % 2 != 1:
		direct = 3


def main():
	pygame.init()
	screen = pygame.display.set_mode([WIDTH, HEIGHT])
	running = True

	while running:
		pygame.time.delay(250)  # 50ms
		move_snake()
		if is_lose():
			gameover_show(screen)
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

	pygame.quit()


if __name__ == '__main__':
	main()
