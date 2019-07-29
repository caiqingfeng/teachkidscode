import turtle
t = turtle.Pen()
turtle.bgcolor("grey")
colors = ["orange", "blue", "white", "black"]
sides = int(turtle.numinput("Number of sides",
                            "How many sides do you want (1-4)?", 4, 1, 8))
for x in range(360):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)