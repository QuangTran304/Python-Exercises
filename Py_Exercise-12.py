# -------------------------------------------------------------------------
#   Author: Quang Tran
#   Date: May 15th, 2019
# -------------------------------------------------------------------------

"""
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the
number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

results = []

for i in range(1000, 3001):
    aString = str(i)
    if (int(aString[0]) % 2 == 0) and (int(aString[1]) % 2 == 0) and (int(aString[2]) % 2 == 0) and (
            int(aString[3]) % 2 == 0):
        results.append(aString)

print(",".join(results))
