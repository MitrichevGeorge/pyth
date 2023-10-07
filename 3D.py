#pip3 install keyboard
import turtle
from math import radians, sin, cos
from time import sleep
#import keyboard
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
screen = turtle.Screen()
screen.tracer(0)

colors = ["red","green","blue"]

#1point 0vector
meshes = [[0,0,0,1],
          [100,0,0,0],
          [0,100,0,0],
          [0,0,100,0]]

#0line
objects = [[0,0,1,0],[0,0,2,1],[0,0,3,2]]

#screen:
slinesp1 = [[]]
slinesp2 = [[]]
scolors = []

#player position:
px = 10
py = 10
pz = -10
prx = 0
pry = 0

#opti:
mrt = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def mmult(val,matr):
    rez=[0,0,0,0]
    for y in range(4):
        for x in range(4):
            rez[y] += (val[x]*matr[y][x])
    return rez

def mmove(x,y,z):
    return[[1,0,0,x],
           [0,1,0,y],
           [0,0,1,z],
           [0,0,0,1]]

def mrotx(rx):
    return[[1,      0,      0,      0],
           [0, cos(rx),-sin(rx),    0],
           [0, sin(rx), cos(rx),    0],
           [0,      0,      0,      1]]

def mroty(ry):
    return[[cos(ry), 0, sin(ry),    0],
           [0,       1,       0,    0],
           [-sin(ry),0, cos(ry),    0],
           [0,      0,      0,      1]]

def mrotz(rz):
    return[[cos(rx),-sin(rx),0,     0],
           [sin(rx), cos(rx),0,     0],
           [0,      0,       1,     0],
           [0,      0,       0,     1]]

def mrotu(rx,ry,rz):
    srx = sin(rx)
    crx = cos(rx)
    sry = sin(ry)
    cry = cos(ry)
    srz = sin(rz)
    crz = cos(rz)
    return[[    cry*crz,                -srz*cry,          sry,     0],
           [srx*sry*crz+srz*crx, -srx*sry*srz+crx*crz, -srx*cry,    0],
           [srx*srz-sry*crx*crz, srx*crz+sry*srz*crx,   srx*cry,    0],
           [        0,                      0,              0,      1]]

def line(_a,_b):
    a = meshes[_a]
    b = meshes[_b]
    if((a[3]==0) and (b[3]==0)):
        print("два вектора не образуют линию. Буфер:",_a,_b)
    else:
        
        
        a = mmult(a,mrotu(prx,pry,0))
        b = mmult(b,mrotu(prx,pry,0))

        a = mmult(a,mmove(-px,-py,-pz))
        b = mmult(b,mmove(-px,-py,-pz))
        if(a[3]):
            slinesp1.append([a[0],a[1]])
            if(b[3]):
                slinesp2.append([b[0],b[1]])
            else:
                slinesp2.append([a[0]+b[0],a[1]+b[1]])
        else:
            slinesp1.append([b[0],b[1]])
            if(a[3]):
                slinesp2.append([a[0],a[1]])
            else:
                slinesp2.append([b[0]+a[0],b[1]+a[1]])

def func():
    slinesp1.clear()
    slinesp2.clear()
    scolors.clear()
    #mrt = mrotu(prx,pry,0)
    for obj in objects:
        if(obj[0]==0):
            line(obj[1],obj[2])
            scolors.append(colors[obj[3]])
    t.clear()
    for i in range(len(slinesp1)):
        #print(slinesp1[i],slinesp2[i])
        t.pencolor(scolors[i])
        t.pu()
        t.goto(slinesp1[i][0],slinesp1[i][1])
        t.pd()
        t.goto(slinesp2[i][0],slinesp2[i][1])
    screen.update()
    
while(1):
    for n in range(360):
        prx = radians(n)
        pry = radians(n)
        func()
        sleep(0.05)

