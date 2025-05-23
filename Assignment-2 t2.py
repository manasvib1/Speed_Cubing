from vpython import *
for x in range(3):
    for y in range(3):
        for z in range(3):
            pos = vector(1.1*x-1,1.1*y-1,1.1*z-1)
            cubelet = box(pos=pos, size=vector(1, 1, 1), color=color.gray(0.5))
            if x==2: box(pos=pos+vector(0.5, 0, 0), size=vector(0.01, 0.9, 0.9), color=color.red)
            if x==0: box(pos=pos-vector(0.5, 0, 0), size=vector(0.01, 0.9, 0.9), color=color.orange)
            if y==2: box(pos=pos+vector(0,0.5,0), size=vector(0.9, 0.01, 0.9), color=color.blue)
            if y==0: box(pos=pos-vector(0,0.5,0), size=vector(0.9, 0.01, 0.9), color=color.green)
            if z==2: box(pos=pos+vector(0, 0, 0.5), size=vector(0.9, 0.9, 0.01), color=color.white)
            if z==0: box(pos=pos-vector(0, 0, 0.5), size=vector(0.9, 0.9, 0.01), color=color.yellow)
while True:
    rate(30)