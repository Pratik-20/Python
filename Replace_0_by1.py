"""
Question 2. Write a Program to replace all 0’s with 1 in a given integer.

Given an integer as an input, all the 0’s in the number has to be replaced with 1.

For example, consider the following number

Input: 102405
Output: 112415

Input: 56004
Output: 56114

DM your Solutions. We will pick the best ans and post here with Your name.
______________________________________________________________________________________
"""
#Answer/Solution Program
#___________________________________________
#Take an integer number as p
p= int(input("Enter a number"))

#Convert an integer number to String as n
n= str(p)

#Now replace 0 by 1
print(n.replace("0", "1"))