# -------------------------------------------------------------------------
#   Author: Quang Tran
#   Date: May 15th, 2019
# -------------------------------------------------------------------------

"""
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""


d = input("Please enter a digit: ")
dd = str(d) + str(d)
ddd = str(d) + str(d) + str(d)
dddd = str(d) + str(d) + str(d) + str(d)

result = int(d) + int(dd) + int(ddd) + int(dddd)
print("Result is: " + str(result))