number_of_pizza = eval(input("how many pizza do you want?"))
prize_of_pizza = eval(input("how much does each pizza cost?"))
the_cost_just_for_pizza = number_of_pizza * prize_of_pizza
tax_rate = 0.08
sales_tax = tax_rate * the_cost_just_for_pizza
total_prize = the_cost_just_for_pizza + sales_tax
print("deer cosumer,you need to pay", total_prize, "for total, and the tax of this delicious dinner is", sales_tax, ",Thank you for coming!")
