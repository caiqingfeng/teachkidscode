import turtle
t = turtle.Pen()
turtle.bgcolor("gray")
colors = ["blue", "black", "orange", "white", "yellow", "green"]
sides = int(turtle.numinput("enter the sides","how many sides do you want?",4, 1, 6))
for x in range(360):
    t.pencolor(colors[x%sides])
    print(x)
    t.forward(x*3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)