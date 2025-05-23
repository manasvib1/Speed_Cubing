from vpython import *
cube=[]
for x in range(3):
    for y in range(3):
        for z in range(3):
            pos = vector(1.1*x-1,1.1*y-1,1.1*z-1)
            face = box(pos=pos, size=vector(1, 1, 1), color=color.white)
            cube.append(face)
while True:
    rate(30)
    for x in cube:
        x.rotate(axis=vec(0, 1, 0), angle=0.01, origin=vec(0, 0, 0))
