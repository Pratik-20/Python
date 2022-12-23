"""
Math functions

The area of a circle


Write a program that reads an integer that represents the radius of a given circle and calculates its area.
To calculate the area of a circle, use the following formula: S=\pi r^2
S=πr^2


Print the result rounded to 2 decimal places.

Sample Input 1:

5
Sample Output 1:

78.54
"""
import math

r = int(input())

s = math.pi * math.pow(r, 2)

print(round(s, 2))
