# -------------------------------------------------------------------------
#   Author: Quang Tran
#   Date: May 10th, 2019
# -------------------------------------------------------------------------

"""
Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all
duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again

Then, the output should be:
again and hello makes perfect practice world
"""


print("Please enter a string: ")
user_input = input().split(" ")
result = []

for word in user_input:
    if word not in result:
        result.append(word)
    else:
        continue


result.sort()
print("\nHere is your new sorted string: ")
print(" ".join(result))


""" 
FASTER WAY -  but does not look clean:
user_input = input().split(" ")
print(" ".join(sorted(list(set(user_input)))))
"""