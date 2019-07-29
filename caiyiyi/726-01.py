driving_age = eval(input("what is the driving_age in your area?"))
your_age = eval(input("how old are you?"))
if your_age >= driving_age:
    print("you are old enough to drive")
else:
    print("you can't drive now")
    years = driving_age - your_age
    print("you have", years, "years to wait before your driving")
print("thanks for useing, have a good day!")

    