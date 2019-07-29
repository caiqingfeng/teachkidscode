import turtle
t=turtle.Pen()
turtle.bgcolor("black")
sides = eval(input("Enter a number of sides between 2 and 8: "))
colors = ["red", "yellow",  "green", "white", "blue", "orange", "purple", "brown"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + 1)
    t.left(360/sides + 1)
    t.width(x*sides/200)
    t.left(90)