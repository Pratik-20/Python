"""
Math functions

Sine and cosine

Write a program that reads a value representing an angle (in radians), and prints the difference between its sine and cosine.

Do not round the result.

Sample Input 1:

0.74
Sample Output 1:

-0.06418064710144289

"""

import math

n = float(input())

print(math.sin(n) - math.cos(n))
