import turtle
t = turtle.Prn()
sides = int(turtle.numinput("number of sides", "how many sides in your spiral"))
for m in range(5,75):
    t.left(360/sides + 5)
    t.width(m//25+1)
    t.penup()
    t.forward(m*4)
    t.pendown()
    if (m%2 == 0):
        for n in range(sides):
            t.circle(m/3)
 
            