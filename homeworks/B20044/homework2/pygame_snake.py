# -*- coding: utf-8 -*-
import pygame
import random

SCALE = 20  #地图中有多少格
SIZE = 20   #每一格的大小
WIDTH = SCALE * SIZE
HEIGHT = SCALE * SIZE

DIRECT = [[0,-1],[-1,0],[0,1],[1,0]]
dirt = 1 #是direct的下标 蛇前进的方向  定义一个初始化方向  向左走



snake = [[4,3],[5,3],[6,3]]
apple = [3,1]

#画蛇和苹果
def screen_show(screen):
    screen.fill([255,255,255])
    for body in snake:
        pygame.draw.rect(screen, [0, 255, 0], [body[0] * SIZE, body[1] * SIZE, SIZE - 1, SIZE - 1])
    pygame.draw.circle(screen, [255, 0, 0], [apple[0]*SIZE + SIZE / 2, apple[1]*SIZE + SIZE / 2], SIZE/2)


    pygame.display.flip()

#让蛇动
def snake_update():
    global dirt
    # 1.当你在函数定义内声明变量的时候，它们与函数外具有相同名称的其他变量没有任何关系，即变量名称对于函数来说是局部的。
    #这称为变量的作用域 。所有变量的作用域是它们被定义的块，从它们的名称被定义的那点开始。

    # 2. 如果你想要为一个定义在函数外的变量赋值，那么你就得告诉Python这个变量名不是局部的，而是全局的。
    # 我们使用global语句完成这一功能。没有global语句，是不可能为定义在函数外的变量赋值的。

    #一、吃不吃到苹果 → 蛇头的坐标都会变
    new_body = [0,0]
    new_body[0] = (snake[0][0] + DIRECT[dirt][0]) % SCALE  #余数scale  能从左边穿墙，后边回来 5%3就得到2
    #              蛇头  的横坐标      取哪一个方向，找到其横坐标

    new_body[1] = (snake[0][1] + DIRECT[dirt][1]) % SCALE
    # 0/20=20*0+0   1/20=20*0+1   19/20=20*0+19  20/20=1+0
    # 0%20=0        1%20=1          19%20=19

    # -1/20=20*(-1)+19   -2/20=20*(-1)+18   -20/20=20*(-1)+0     -21/20=20*(-2)+19
    #   -1%20=19            -2%20=18          -20%20=0             -21%20=19


    # 二、尾的变化
    #1.吃到苹果→蛇头变，不砍掉尾 → 蛇头（苹果位置）+原来的蛇身
    if new_body == apple:
        snake.insert(0, new_body) #（要插入的位置的index，插入的值） 意思是在蛇头插入new_body
        # insert()函数用于将指定对象插入列表的指定位置。
        # list.insert(index, obj)
        # index - - 对象obj需要插入的索引位置。 obj - - 要插入列表中的对象。
        # 该方法没有返回值，但会在列表指定位置插入对象。

        # aList = [123, 'xyz', 'zara', 'abc']
        # aList.insert(3, 2009)
        # List: [123, 'xyz', 'zara', 2009, 'abc']
        return True

  #2.正常行走，头变，砍尾
    else:
        snake.insert(0, new_body)
        # 砍掉蛇身体的最后一截
        snake.pop()
        return False

        #pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
        # aList = [123, 'xyz', 'zara', 'abc'];
        # print "A List : ", aList.pop();    # AList:  abc  删掉最后一个
        # print "B List : ", aList.pop(2);   # BList:  zara  删掉index=2的值

#当蛇吃到苹果时，重新生成苹果
def new_apple():
    apple[0]=random.randint(0,19)
    apple[1]=random.randint(0,19)


#蛇咬到了自己→有2个蛇头：
def is_lose():
    if snake.count(snake[0]) >2:
        return True
    return False





#修改dirt蛇的前进方向即可（默认向左）

# ≠1,3 →1,3
# # 1. !=为不等于  ==0时，运动方向为上下0,2
# 所以当≠0，即为左右方向1,3运动时，才可以向上下0,2运动
def w_down_cb():
    global dirt
    if dirt%2 !=0:
        dirt = 0

def s_down_cb():
    global dirt
    if dirt % 2 != 0:
        dirt = 2
 # ≠0,2 →0,2
# %2==1时，左右1,3运动  ！=1 为上下0,2运动  dirt=0,2上下运动时→ 1,3向左右运动
def a_down_cb():
    global dirt
    if dirt % 2 != 1:
        dirt = 1

def d_down_cb():
    global dirt
    if dirt % 2 != 1:
        dirt = 3

def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    running  = True

    while running:
        pygame.time.delay(200) # 50ms
        if snake_update():
            new_apple()

        # 如果吃到自己，直接退出
        if is_lose():
            break


        screen_show(screen)
        # 每次都记得把screenshow放在最后

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
