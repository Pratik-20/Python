"""
Free air miles
Imagine you have a credit card with a free air miles bonus program (or maybe you already have one).
As a user, you are expected to input the amount of money you spend on average from this card per month.
Let's assume that the bonus program gives you 2 free air miles for every dollar you spend.' \
Here's a simple program to figure out when you can travel somewhere for free:
"""

# the average amount of money per month
money = int(input("How much money do you spend per month: "))

# the number of miles per unit of money
n_miles = 2

# earned miles
miles_per_month = money * n_miles

# the distance between London and Paris
distance = 215

# how many months do you need to get
# a free trip from London to Paris and back
print(distance * 2 / miles_per_month)

#This program will calculate how many months it takes to travel the selected distance and back.