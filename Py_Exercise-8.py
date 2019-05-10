# -------------------------------------------------------------------------
#   Author: Quang Tran
#   Date: May 10th, 2019
# -------------------------------------------------------------------------

"""
Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
"""


list_of_words = input("Please enter some strings, separated by commas: ").split(",")
list_of_words.sort()
print(",".join(list_of_words))
