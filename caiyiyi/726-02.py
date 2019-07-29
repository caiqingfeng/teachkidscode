shape = input("what shape do you want?p/r")
if shape == "p":
    import turtle
    t = turtle.Pen()
    sides = int(turtle.numinput("the number of sides", "how many sides do you want?"))
    for x in range(sides):
        t.forward(10)
        t.left(360/sides)
else:
    import turtle
    t = turtle.Pen()
    number = int(turtle.numinput("number of circles", "how many circles do you what"))
    for x in range(number):
        t.circle(100)
        t.left(360/number)

