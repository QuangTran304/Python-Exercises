# -------------------------------------------------------------------------
#   Author: Quang Tran
#   Date: May 10th, 2019
# -------------------------------------------------------------------------

"""
Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether
they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example:
0100,0011,1010,1001

Then the output should be:
1010

Notes: Assume the data is input by console.
"""


print("Please enter some binary numbers, separated by commas:")
user_input = input().split(",")
valid_elements = []

for e in user_input:
    if int(e, 2) % 5 == 0:
        valid_elements.append(e)


print("\nResult: ")
print(",".join(valid_elements))