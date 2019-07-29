import turtle
t = turtle.Pen()
colors = ["blue", "purple", "white", "yellow", "grey"]
family = []
name = turtle.textinput("my family", "enter a name or just hit[ENTER] to quit")
turtle.bgcolor("black")
while name != "":
    family.append(name)
    name = turtle.textinput("my family", "enter a name or just hit[ENTER] to quit")
for x in range(100):
    t.pencolor(colors[x%len(family)])
    t.penup()
    t.forward(x*4)
    t.pendown
    t.write(family[x%len(family)], font = ("Arial", int((x+4)/4), "bold"))
    t.left(360/len(family) + 2)