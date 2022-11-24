"""
Work on project. Stage 2/5: New rules

New rules

Description
Your friend's suggestion surprised you a little bit. After a couple of "No, you" retaliations, you decided that it would be more convenient to input the initial conditions to determine who goes first, and how many pencils there are on the table.

Objectives
Write a program that will satisfy the conditions below:

Ask users to input the number of pencils with the How many pencils string. Read the number;
Ask users to input who goes first from the two possible players. To do so, output the Who will be the first (*Name1*, *Name2*) string. You can ask a user to choose from any two names that consist of the letters of the English alphabet and numbers (for example, John and Jack). Read the name;
Print two lines: one with vertical bar symbols representing the input number of pencils, the other with the *NameX* is going first string.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input. Player names are given for reference.Example 1:

How many pencils would you like to use:
> 5
Who will be the first (John, Jack):
> John
|||||
John is going first!
Example 2:

How many pencils would you like to use:
> 20
Who will be the first (John, Jack):
> Jack
||||||||||||||||||||
Jack is going first!
"""



n = int(input("How many pencils would you like to use:"))
l = "|"

print("Who will be the first (John, Jack):")
name = str(input())

print(l * n)
print(f'{name} is going first!'.format(name))
