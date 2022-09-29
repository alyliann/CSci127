#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: November 9, 2021
#This program tests whether the inputted integer is a valid square

import math

def is_square(positive_int):
    if positive_int < 0:
        return False
    root = math.sqrt(positive_int)
    return positive_int == int(root + 0.5) ** 2

def perfectSquareChecker(num):
    if not (is_square(num)):
        print("Hey, this number isn't even! Try again next time.")
        return False

    print("This number is a perfect square, it is the product of:", math.sqrt(num), "squared.")

def main():

    """
    You are provided the above two functions, your job now is to take
    user input and validate it. In other words, take integer input from
    the user, and make sure that it is a perfect square. If it's not,
    you need to keep asking the user for a perfect square until they
    enter one.
    Hint, you should use a while loop to validate input!
    Another hint, you are provided the function (is_square) which will
    check to see if a positive integer is a perfect square or not!
    """
    num = int(input("Enter a square integer: "))
    while is_square(num) == False:
        if perfectSquareChecker(num) == False:
             num = int(input("Enter a square integer: "))
    else:
        print("This number is a perfect square. It is the product of:", math.sqrt(num), "squared.")

if __name__ == "__main__":
    main()
