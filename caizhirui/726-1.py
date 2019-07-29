import turtle
t = turtle.Pen()
turtle.bgcolor("purple")
colors = ["white", "yellow"]
number_of_circles = int(turtle.numinput("Number of circle", "How many circle in your rosette?",20))
for x in range(number_of_circles):
    t.pencolor(colors[0])
    t.circle(100)
    t.pencolor(colors[1])
    t.circle(50)
    t.left(360/number_of_ci bujnh