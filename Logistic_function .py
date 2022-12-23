"""
Math functions

Logistic function

Write a program that reads an integer and calculates the value of its logistic function.
A logistic function, or sigmoid function, is a function defined by the formula \sigma(x) = \frac{1}{1 + e^{-x}} = \frac{e^x}{e^{x} + 1}
σ(x)=1/(1+e^(−x)) = e^x/((e^x)+1)


Print the result rounded to 2 decimal places.

You can use math.e constant equal to 2.718281… or sort of a shortcut math.exp(x) function, which is considered more accurate than math.e ** x or pow(math.e, x).
 
Sample Input 1:

81
Sample Output 1:

1.0
"""
# put your python code here
import math

x = int(input())

n = 1 / (1 + math.exp(-x))

print(round(n, 2))
