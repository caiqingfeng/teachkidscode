import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "gray", "white", "blue"]
your_name = turtle.textinput("enter your name","what's your name")
for x in range(100):
    t.pencolor(colors[x%4])
    t.penup()
    t.forward(x*3/2 + x)
    t.pendown()
    t.write(your_name, font = ("Arial", int((x+4)/4), "bold"))
    t.left(360/2 + 1)