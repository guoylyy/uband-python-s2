# -*- coding: utf-8 -*-
import pygame
#只左右移动
MOU_CON = True

board = pygame.Rect(280, 400, 80, 5)  #方块

circle = [100, 100] #球心
RADIUS = 10
SPEED = [5, 5]
WIDTH = 640
HEIGHT = 480

def renew_ball():
	if circle[1] > HEIGHT:
		circle[0] = 100
		circle[1] = 100


def update_ball():
	if circle[1] - RADIUS == 0: #撞击上边缘
		SPEED[1] *= -1 
	if circle[0] + RADIUS == WIDTH or circle[0] - RADIUS == 0:
		SPEED[0] *= -1
	if circle[1] + RADIUS == board.top and board.left <= circle[0] <= board.right:
		SPEED[1] *= -1 
	circle[0] += SPEED[0]
	circle[1] += SPEED[1]

def draw_surface(screen):
	#每次都要重新fill，否则画布会叠加
	screen.fill([255,255,255]) #设置画布颜色 R G B
	pygame.draw.circle(screen,[255,0,0],circle,RADIUS) #surface，颜色，圆心，半径，0=圆球 1=像素为1的圆环
	pygame.draw.rect(screen,[0,255,255],board) #surface,color,(x,y,width,height)
	pygame.display.flip() #显示

def update_board():
	if MOU_CON:
		(x, y) = pygame.mouse.get_pos() #获取鼠标位置信息，范围值是tuple
		board.centerx = x #方块根据鼠标位置移动
		#board.centery = y

def w_down_ch():
	if not MOU_CON:
		#board.centery -= 5 #注意y轴向下为正
		pass

def s_down_ch():
	if not MOU_CON:
		#board.centery += 5 
		pass

def a_down_ch():
	if not MOU_CON:
		board.centerx -= 5 		

def d_down_ch():
	if not MOU_CON:
		board.centerx += 5 

def main():
	pygame.init()
	screen = pygame.display.set_mode([WIDTH,HEIGHT]) 
	running = True

	while running:
		pygame.time.delay(50) #每次循环延迟时间，毫秒
		update_board()
		update_ball() 
		renew_ball()
		draw_surface(screen)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN: #按键事件
				if event.key == pygame.K_w: #w键
					w_down_ch() #call_back 回调函数
				elif event.key == pygame.K_s: 
					s_down_ch() 
				elif event.key == pygame.K_a: 
					a_down_ch() 
				elif event.key == pygame.K_d: 
					d_down_ch() 
if __name__ == '__main__':
	main()
