# Exercise 6: Tax and Tip
# The program that you create for this exercise will begin by reading the cost
# of a meal ordered at a restaurant from the user. Then your program will
# compute the tax and tip for the meal. Use your local tax rate when computing
# the amount of tax owing. Compute the tip as 18 percent of the meal amount
# (without the tax). The output from your program should include the tax
# amount, the tip amount, and the grand total for the meal including both the
# tax and the tip. Format the output so that all of the values are displayed
# using two decimal places.


def calculate_tax(cost):
    tax_rate_in_percent = 15
    tax_amount = cost * tax_rate_in_percent / 100
    return tax_amount, tax_rate_in_percent


def calculate_tip(cost):
    tip_rate_in_percent = 18
    tip_amount = cost * tip_rate_in_percent / 100
    return tip_amount, tip_rate_in_percent


if __name__ == "__main__":
    meal_cost = float(input("Enter Meal Cost: "))
    tax_amount, tax_rate = calculate_tax(meal_cost)
    tip_amount, tip_rate = calculate_tip(meal_cost)
    total_bill = meal_cost + tax_amount + tip_amount
    print("Tax Amount (@%4.2f%%)\t:%10.2f" % (tax_rate, tax_amount))
    print("Tip Amount (@%4.2f%%)\t:%10.2f" % (tip_rate, tip_amount))
    print("Total Bill\t\t:%10.2f" % total_bill)
