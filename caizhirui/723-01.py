import turtle
t = turtle.Pen()
turtle.bgcolor("grey")
colors = ["orange", "blue", "black", "white"]
your_name = turtle.textinput("Enter your name", "What is your name?")
for x in range(1000):
    t.pencolor(colors[x%4])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(your_name, font = ("Arial", int( (x + 4) / 4), "bold") )
    t.left(95)