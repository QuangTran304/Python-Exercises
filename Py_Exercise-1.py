#-------------------------------------------------------------------------
#   Author: Quang Tran
#   Date: May 9th, 2019
#-------------------------------------------------------------------------


"""
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

aList = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        aList.append(str(i))


print(", ".join(aList))         # Use a string to join all the elements in the list