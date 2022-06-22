from cmath import pi
from turtle import *
speed(0)


def drawleaf():
    down()
    begin_fill()
    circangle = heading()
    width(1)
    seth(heading()+230)
    circle(40, 80)
    seth(heading()+100)
    circle(40, 80)
    seth(circangle)
    end_fill()
    up()

def drawsideleaf():
    down()
    begin_fill()
    circangle = heading()
    width(1)
    seth(heading()+180)
    circle(40, 80)
    seth(heading()+100)
    circle(40, 80)
    seth(circangle)
    end_fill()
    up()

def drawothersideleaf():
    down()
    width(1)
    fillcolor("white")
    begin_fill()
    circangle = heading()
    width(1)
    seth(heading()+280)
    circle(40, 80)
    seth(heading()+100)
    circle(40, 80)
    seth(circangle)
    end_fill()
    up()

def smalldot(wd):
    down()
    width(wd)
    circle(1)
    width(1)
    up()


def ypos():
    y = abs(ycor()) + 8
    return y


def dotline():

    ndots = (2 * ypos() * pi)/17.4
    ndot = 0
    y = ypos()
    while ndot < ndots:
        circle(y, (360/ndots))
        smalldot(10)
        ndot += 1

    setpos(0, ycor() - 3)
    seth(0)
    width(5)
    down()
    circle(ypos())
    up()

def drawdiamond():
    ang = heading()
    fillcolor("white")
    begin_fill()
    down()
    right(45)
    forward(10)
    n=0
    while n<3: 
        left(90)
        forward(10)
        n+=1
    end_fill()
    seth(ang)

    up()

up()
setposition(0, 8)
ht()

smalldot(20)

goto(xcor(), ycor()-20)
seth(0)

nleaves = 0
while nleaves < 8:
    drawleaf()
    circle(20, 45)
    nleaves += 1

setpos(xcor(), ycor() - 30)

ndot = 0
circle(50, 22.5)

while ndot < 8:
    smalldot(5)
    circle(50, 45)
    ndot += 1

setpos(0, ycor() - 40)
seth(0)

dotline()

setpos(0, ycor() - 35)
down()
width(3)
circle(ypos())
up()

setpos(0, ycor()+23)
y= ycor() - 8
nleaves = 0
while nleaves < 16:
    drawsideleaf()
    circle(-y, 360/16)
    nleaves += 1

setpos(0, ycor())
y= ycor() - 8
nleaves = 0
while nleaves < 16:
    drawothersideleaf()
    circle(-y, 360/16)
    nleaves += 1


setpos(0, ycor() - 58)
seth(0)

dotline()

setpos(0, ycor() - 25)
seth(0)
width(40)
pd()
begin_fill()
circle(ypos())
pu()
width(1)

y=ycor()-8
setpos(0, ycor())
seth(0)
ndia =0
while ndia <= 64:
    drawdiamond()
    circle(-y, 360/64)
    ndia += 1



exitonclick()
