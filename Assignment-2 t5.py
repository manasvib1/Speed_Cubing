from vpython import *

base=box(pos=vector(0,0,0),size=vector(3,1,2), color=color.yellow)

c1=cylinder(pos=vector(-1,0.5,0.5),axis=vector(0,0.4,0),radius=0.3,color=color.white)
c2=cylinder(pos=vector(1,0.5,0.5),axis=vector(0,0.4,0),radius=0.3,color=color.white)
c3=cylinder(pos=vector(0,0.5,0.5),axis=vector(0,0.4,0),radius=0.3,color=color.white)
c4=cylinder(pos=vector(-1,0.5,-0.5),axis=vector(0,0.4,0),radius=0.3,color=color.white)
c5=cylinder(pos=vector(1,0.5,-0.5),axis=vector(0,0.4,0),radius=0.3,color=color.white)
c6=cylinder(pos=vector(0,0.5,-0.5),axis=vector(0,0.4,0),radius=0.3,color=color.white)
brick=compound([base,c1,c2,c3,c4,c5,c6])
while True:
    rate(30)
    brick.rotate(axis=vec(0, 1, 0), angle=0.01, origin=vec(0, 0, 0))    