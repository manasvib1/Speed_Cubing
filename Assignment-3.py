from vpython import *
cube=[]
for x in range(3):
    for y in range(3):
        for z in range(3):
            pos = vector(1.1*x-1.1,1.1*y-1.1,1.1*z-1.1)
            face = box(pos=pos, size=vector(1, 1, 1), color=color.white)
            cube.append(face)
def update_layers():
    global top,right,front,bottom,left,back
    top = [c for c in cube if round(c.pos.y, 1) == 1.1]
    right = [c for c in cube if round(c.pos.x, 1) ==  1.1]
    front = [c for c in cube if round(c.pos.z, 1) ==  1.1]
    bottom = [c for c in cube if round(c.pos.y, 1) == -1.1]
    left = [c for c in cube if round(c.pos.x, 1) ==  -1.1]
    back = [c for c in cube if round(c.pos.z, 1) ==  -1.1]
update_layers()
def top_rotate(cubef):
   for _ in range(25):
      rate(60)
      for c in cubef:
         c.rotate(axis=vec(0,1,0), angle=-pi/50, origin=vec(0,1.1,0))
   update_layers()
def bottom_rotate(cubef):
   for _ in range(25):
      rate(60)
      for c in cubef:
         c.rotate(axis=vec(0,1,0), angle=pi/50, origin=vec(0,-1.1,0))
   update_layers()
def right_rotate(cubef):
   for _ in range(25):
      rate(60)
      for c in cubef:
         c.rotate(axis=vec(1,0,0), angle=-pi/50, origin=vec(1.1,0,0))
   update_layers()  
def left_rotate(cubef):
   for _ in range(25):
      rate(60)
      for c in cubef:
         c.rotate(axis=vec(1,0,0), angle=pi/50, origin=vec(-1.1,0,0))
   update_layers()      
def front_rotate(cubef):
   for _ in range(25):
      rate(60)
      for c in cubef:
         c.rotate(axis=vec(0,0,1), angle=-pi/50, origin=vec(0,0,1.1))
   update_layers()   
def back_rotate(cubef):
   for _ in range(25):
      rate(60)
      for c in cubef:
         c.rotate(axis=vec(0,0,1), angle=pi/50, origin=vec(0,0,-1.1))
   update_layers()   
def keyInput(evt):
    s=evt.key.lower()
    if s=='j':
        top_rotate(top)
    elif s=='k':
        right_rotate(right)
    elif s=='s':
       bottom_rotate(bottom)
    elif s=='d':
        left_rotate(left)
    elif s=='h':
        front_rotate(front)
    elif s=='w':
       back_rotate(back)
    
scene.bind('keydown', keyInput)
while True:
    rate(60)
