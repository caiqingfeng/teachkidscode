import turtle
answer = input("do you what to see a spiral?y/n")
if answer == 'y':
    t = turtle.Pen()
    sides = int(turtle.numinput("number of sides", "how many sides do you want?"))
    for x in range(100):
        t.forward(x*3 / sides + x)
        t.left(360 / sides + 1)
print("now we've done thanks for paying！")