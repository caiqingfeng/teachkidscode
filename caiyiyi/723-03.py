import turtle
turtle.bgcolor("purple")
number = int(turtle.numinput("enter your number of circles", "how many circles do you want?"))
t = turtle.Pen()
colors = ["white", "yellow"]
for x in range(number):
    t.pencolor(colors[0])
    t.circle(100)
    t.pencolor(colors[1])
    t.circle(50)
    t.left(360/number)