# -*- coding: utf-8 -*-

import pygame
def main():
	pygame.init()#初始化pygame,为使用硬件做准备
	screen = pygame.display.set_mode([640,480])#相当于生成画布，像素点原点在左上角，右向0-640为x轴，下向0-480为y轴
	running = True
	while running:
		screen.fill([255,255,255]) #设置填充颜色，三个数字分别代表红、绿、蓝色分量 0-255，都是255——白色
		pygame.draw.circle(screen,[255,0,0],[100,100],10,0)#1.color2.圆心在x、y轴的位置3.半径4.是圆环(数字代表圆环粗细)还是圆(0)
		pygame.draw.rect(screen,[0,255,255],[280,400,80,5],0)#1.color2.[左上角顶点坐标，宽度W，高度H]3.0-实心长方形，其他数字代表长方形边框的粗细
		

		# pygame.draw.circle(screen,[100,100,200],[320,240],50,5)
		# pygame.draw.circle(screen,[0,0,250],[320,240],30,0)
		# pygame.draw.rect(screen,[50,150,50],[270,400,100,30],5)
		# pygame.draw.rect(screen,[200,50,50],[290,405,60,20],0)

		pygame.display.flip()#把填充的东西全部运行在screen上
		for event in pygame.event.get():
			if event.type == pygame.QUIT:#点右上角叉叉关闭的话
				running = False
	pygame.quit()

if __name__ == '__main__':
	main()