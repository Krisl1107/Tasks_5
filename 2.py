import turtle
xc=int(input("xc="))
yc=int(input("yc="))
r=int(input("r="))
x=int(input("x="))
y=int(input("y="))

a=((x-xc)**2 + (y-yc)**2)**1/2
if a>x :
    point="Точка внутри круга"
else:
    point="Точка вне круга"

turtle.up()
turtle.goto(xc, yc-r)
turtle.down()
turtle.circle(r)


turtle.up()
turtle.goto(x, y)
turtle.down()
turtle.dot(size=5)

turtle.up()
turtle.setposition(100,-100)
turtle.write(f"{point}")


turtle.done()
