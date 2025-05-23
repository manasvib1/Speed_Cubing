from vpython import *
cube=[]
cubelet = box(pos=vector(0,0,0), size=vector(1, 1, 1), color=color.white)
cubelet = box(pos=vector(0,1,0), size=vector(1, 1, 1), color=color.green)
cubelet = box(pos=vector(0,2,0), size=vector(1, 1, 1), color=color.yellow)
cubelet = box(pos=vector(0,3,0), size=vector(1, 1, 1), color=color.red)
cubelet = box(pos=vector(0,4,0), size=vector(1, 1, 1), color=color.blue)
cube.append(cubelet)
while True:
    rate(30)