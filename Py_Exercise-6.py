# -------------------------------------------------------------------------
#   Author: Quang Tran
#   Date: May 9th, 2019
# -------------------------------------------------------------------------


"""
Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""

import math


def Q():
    C = 50
    H = 30
    listOfResults = []
    userInput = input("Please enter some numbers, separated by commas: ").split(",")

    for D in userInput:
        result = math.sqrt((2 * C * int(D)) / H)
        listOfResults.append(str(int(result)))

    print(",".join(listOfResults))


Q()
