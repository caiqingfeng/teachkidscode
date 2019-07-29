import turtle
t = turtle.Pen()
t.penup()
turtle.bgcolor("black")
sides = int(turtle.numinput("number of sides", "how many sides do you want?", 4, 2, 6))
colors = ["yellow", "white", "blue", "grey", "brown"]
for x in range(100):
    t.forward(x*4)
    position = t.position()
    print(position)
    heading = t.heading()
    print(heading)
    for y in range(int(x/2)):
        t.pendown()
        t.pencolor(colors[y%sides])
        t.forward(y*2)
        t.right(360/sides - 2)
        t.penup()
    t.setx(position[0])
    t.sety(position[1])
    t.setheading(heading)
    t.left(360/sides + 2)
    
    