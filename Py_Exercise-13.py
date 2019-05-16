# -------------------------------------------------------------------------
#   Author: Quang Tran
#   Date: May 15th, 2019
# -------------------------------------------------------------------------

"""
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123

Then, the output should be:
LETTERS 10
DIGITS 3
"""

user_input = input("Please input something: ")
alpha_counter = 0
digit_counter = 0

for e in user_input:
    if not e.isspace():
        if e.isalpha():
            alpha_counter += 1
        else:
            digit_counter += 1

print("Digit: {}".format(digit_counter))
print("Alpha: {}".format(alpha_counter))