# viralSpiral

import turtle
t = turtle.Pen()
t.penup()
turtle.bgcolor("grey")
sides = int(turtle.numinput("number of sides", 
        "How many sides in your spiral of spirals? (2-6)", 4, 2, 6))
colors = ["purple", "blue", "white", "black", "orange", "red"]

for m in  range(100):
    t.forward(m*4)
    position = t.position()
    heading = t.heading()
    print(position, heading)

    for n in range(int(m/2)):
        t.pendown()
        t.pencolor(colors[n%sides])
        t.forward(2*n)
        t.right(360/sides -2)
        t.penup()
    t.setx(position[0])
    t.sety(position[1])
    t.setheading(heading)
    t.left(360/sides + 2)