"""
Math functions

Heron's formula

Many years ago, when Paul went to school, he did not like using Heron's formula to calculate the area of a triangle, because he considered it to be very complex. One day he decided to help all the students in his school by writing a program that calculated the area of a triangle by its three sides.

However, there was a problem: as Paul did not like the formula, he did not memorize it. Help him finish this act of kindness and write the program following Heron's formula:

S=\sqrt{p(p - a)(p - b)(p - c)}

S= p(p−a)(p−b)(p−c)
​

where p=\dfrac{a + b + c}2
p=
2
a+b+c
​

 is a half-perimeter of the triangle. On the input, the program has integers,
 and the output should be a real number corresponding to the area of the triangle.

Do NOT round the result.

 Report a typo
Sample Input 1:

3
4
5
Sample Output 1:

6.0
"""
# put your python code here
from math import sqrt

def half_perimeter(a, b, c):
    return (a + b + c) / 2


def area(a, b, c):
    p = half_perimeter(a, b, c)
    return sqrt(p * (p - a) * (p - b) * (p - c))


print(area(int(input()), int(input()), int(input())))
