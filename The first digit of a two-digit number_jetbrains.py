"""
Program with numbers

The first digit of a two-digit number

Write a program that takes a two-digit integer as an input and prints its first digit (i.e., the number of tens).

Sample Input 1:
42

Sample Output 1:
4
"""



# put your python code here
n = int(input())
if n <= 99:
    print(int(n / 10))