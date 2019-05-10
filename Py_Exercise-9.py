# -------------------------------------------------------------------------
#   Author: Quang Tran
#   Date: May 10th, 2019
# -------------------------------------------------------------------------

"""
Question
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence
capitalized.

Suppose the following input is supplied to the program:
Hello world
Practice makes perfect

Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""


lines_entered = []
print("Please enter some sentences. Hit enter one more time when finish: ")

while True:
    user_input = input()
    if user_input != "":
        lines_entered.append(user_input.upper())
    else:
        break


for line in lines_entered:
    print(line)
