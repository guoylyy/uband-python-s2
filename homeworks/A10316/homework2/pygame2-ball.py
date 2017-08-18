# -*- coding: UTF-8 -*-


import pygame

MOU_CON = True

board = pygame.Rect(280, 400, 80, 5)  #弹球的板
circle = [100, 100] #球的圆心位置
RADIUS = 10   #求的半径
speed = [5, 5]
WIDTH = 640
HEIGHT = 480

def renew_ball():
	if circle[1] > HEIGHT:
		circle[0] = 100
		circle[1] = 100

def update_ball():  #更新球的位置
	if circle[1] - RADIUS == 0:    #碰撞到上边缘（小球圆心减去半径等于0） 
		speed[1] *= -1             #那么y轴的方向发生了变化
	if circle[0] + RADIUS ==WIDTH or circle[0] - RADIUS ==0:  #碰撞右边缘
		speed[0] *= -1             #x轴速度发生变化
	# if circle[0] - RADIUS ==0:     #和碰右边缘是一样的 所以直接合并成一条
		# speed[0] *= -1
	if circle[1] + RADIUS == 400 and circle[0] >= board[0] and circle[0] <= board[0] + 80 :    #圆心加半径等于小板子的y轴
		speed[1] *= -1

	circle[0] += speed[0]     #x轴 加速度
	circle[1] += speed[1]     #y轴 加速度


def draw_surface(screen):
	screen.fill([255, 255, 255])     #white   每一个动作后重新填充了一遍画布
	pygame.draw.circle(screen, [255, 0, 0], circle, RADIUS)
	pygame.draw.rect(screen, [0, 255, 255], board)    
	pygame.display.flip()
	
def update_board():
	if MOU_CON:
		(x, y) = pygame.mouse.get_pos()   #获取鼠标的位置信息
		board.centerx = x   #板的x轴中心跟着鼠标的中心走
		# board.centery = y    #全板移动

def fail():
	if circle[1] > HEIGHT:
		return True
	return False

def w_down_cb():
	# if not MOU_CON:
	# 	board.centery -= 5    #y轴是向下加的 往上走得用减
	pass

def s_down_cb():
	# if not MOU_CON:
		# board.centery += 5
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
		pygame.time.delay(40)   #50是毫秒
		update_board()   #根据鼠标输入更新弹球板的位置
		update_ball()
		draw_surface(screen)   #对于画布表面的设置都打包成一个函数

		if fail():
			break

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
	
	pygame.quit()  

if __name__ == '__main__':
	main()
	