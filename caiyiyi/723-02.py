print("what's the problem?")
problem = input("enter a math problem,or 'q'to quit:")
while (problem != "q"):
    print("the answer to", problem, "is:", eval(problem))
    problem = input("enter a math problem,or 'q'to quit:")
    