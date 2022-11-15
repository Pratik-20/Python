"""
Desks

A school has decided to create three new math groups and equip three classrooms for them with new desks.
Your task is to calculate the minimum number of desks to be purchased. To do so, you'll need the following information:

The number of students in each of the three groups is known: your program will receive three non-negative integers as the input.
It is possible that one or more of them will be zero, so you should take it into account.
Each group will sit in its own classroom.
It means that you should calculate the number of desks for each classroom separately, and only then add them up!
At most two students may sit at any desk.
You are expected to output the minimum number of desks to buy, so there should be as many as possible desks taken by two students rather than one.
Most probably, you'll need operations // and % in your program!

Sample Input 1:

20
21
22

Sample Output 1:

32
Sample Input 2:

16
18
20

Sample Output 2:

27

"""
# python code

m = int(input())   # group 1
n = int(input())   # group 2
o = int(input())   # group 3

d = (int((m // 2) + (n // 2) + (o // 2)))  # division
r = (int((m % 2) + (n % 2) + (o % 2)))     # reminder

print(d + r)