"""
Indexes

Сalculator

Medium

A calculator stores the result of the previous calculations in its memory as a list.
You want to access the last calculation, but you don't know how many calculations there were in total.

Work with the calculations variable and print the last calculation.

Sample Input 1:

12 34 56 78 97 45 23 67

Sample Output 1:

67
"""






calculations = input().split()
n = len(calculations)
print(n)
print(calculations[n-1])