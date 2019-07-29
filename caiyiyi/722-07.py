import turtle
turtle.bgcolor( "black" )
t = turtle.Pen()
colors = ["red", "yellow", "blue", "green"]
for x in range(100):
    print("x=", x)
    t.pencolor(colors[x%4])
    print("x%4=", x%4)
    print("color=", colors[x%4])
    t.circle(x)
    t.left(91)