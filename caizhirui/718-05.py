import turtle
t=turtle.Pen()
turtle.bgcolor("grey")
colors = ["blue", "green","red","yellow"]
for x in range(1000):
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(91)