#!/usr/bin/python
#coding: UTF-8

import turtle
import time

# 调用turtle中的Pen函数创建画布
t = turtle.Pen()
# 画矩形
for i in range(0, 4):
	# 往前画一条直线
	t.forward(100)
	# 左转弯90度
	t.left(90)
	time.sleep(1)

#time.sleep(3)
# 清空画布并把海龟放在起始位置
t.reset()

# 画两条相互平行的直线

# 往后画一条直线
t.backward(100)
# 拿起画笔，不再作画，只有遇见down函数的时候才可以继续作画
t.up()
# 右转90度
t.right(90)
# 往前移动20个像素
t.forward(20)
# 左转90度，指向和上一条线平行的方向
t.left(90)
# 放下画笔，开始作画
t.down()
# 画另一条平行线
t.forward(100)
#time.sleep(3)

t.reset()

#画等边三角形
t.forward(100)
t.left(120)
t.forward(100)
t.right(60)
t.backward(100)

time.sleep(3)

# 只清空画布，海龟仍然停留在当前的位置
#注意此时箭头所在的位置，注意与reset执行时的区别
t.clear()