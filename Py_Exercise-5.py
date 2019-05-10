# -------------------------------------------------------------------------
#   Author: Quang Tran
#   Date: May 9th, 2019
# -------------------------------------------------------------------------


"""
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""


class MyClass:
    def __init__(self):
        self.aString = ""

    def getString(self):
        self.aString = input("Please enter something: ")
        return self.aString

    def printString(self):
        print("You have just entered: " + self.aString.upper())


myObj = MyClass()
myObj.getString()
myObj.printString()