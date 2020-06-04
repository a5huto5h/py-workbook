# Exercise 5: Bottle Deposits
# In many jurisdictions a small deposit is added to drink containers to
# encourage people to recycle them. In one particular jurisdiction, drink
# containers holding one liter or less have a $0.10 deposit, and drink
# containers holding more than one liter have a $0.25 deposit.
# Write a program that reads the number of containers of each size from the
# user. Your program should continue by computing and displaying the refund
# that will be received for returning those containers. Format the output so
# that it includes a dollar sign and always displays exactly two decimal
# places.


def calculate_refund(one_liter, more_liter):
    one_liter_refund = 0.10
    more_liter_refund = 0.25
    return one_liter * one_liter_refund + more_liter * more_liter_refund


if __name__ == "__main__":
    one_liter = float(input("1 liter containers: "))
    more_liter = float(input("1+ liter containers: "))
    print("Refund Amount is $%.2f" % calculate_refund(one_liter, more_liter))
