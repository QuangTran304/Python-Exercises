# -------------------------------------------------------------------------
#   Author: Quang Tran
#   Date: May 15th, 2019
# -------------------------------------------------------------------------

"""
Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!

Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""

user_input = input("Please enter something: ")
upper_counter = 0
lower_counter = 0

for e in user_input:
    if not e.isspace():
        if e.isupper():
            upper_counter += 1
        elif e.islower():
            lower_counter += 1
        else:
            pass

print("Upper: {}".format(upper_counter))
print("Lower: {}".format(lower_counter))