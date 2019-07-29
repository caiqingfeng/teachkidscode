import turtle
t=turtle.Pen()
turtle.bgcolor("gold")
sides = 3
colors = ["red",  "white", "blue"]
for x in range(45nh): eber
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + 1)
    t.left(90/sides + 1)
    t.width(x*sides/200)