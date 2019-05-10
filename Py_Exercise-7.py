# -------------------------------------------------------------------------
#   Author: Quang Tran
#   Date: May 10th, 2019
# -------------------------------------------------------------------------

"""
Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th
row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""

aList = []


def array2D(x, y):
    for i in range(x):
        innerList = []

        for j in range(y):
            innerList.append(j * i)

        aList.append(innerList)
    print(aList)


userInput = input("Please enter 2 integers, separated by a comma: ").split(",")
firstInput = int(userInput[0])
secondInput = int(userInput[1])

array2D(firstInput, secondInput)
