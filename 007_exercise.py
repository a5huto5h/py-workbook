# Exercise 7: Sum of the First n Positive Integers
# Write a program that reads a positive integer, n, from the user and then
# displays the sum of all of the integers from 1 to n.


def sum_of_n_integers(n):
    return n * (n + 1) / 2


if __name__ == '__main__':
    num = int(input("Enter the number: "))
    sum_num = sum_of_n_integers(num)
    print("Sum of first %d numbers is %d" % (num, sum_num))
