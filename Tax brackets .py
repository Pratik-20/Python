"""
String formatting

Tax brackets
Hard

Whoa! This problem is much more complex than the usual one and requires knowledge of if-elif-else statements.
If you're feeling up to the challenge, brace yourself and good luck! Otherwise, you can skip it for now and return any time later
In progressive tax systems, tax rates change according to the income. Tax brackets are divisions that regulate those changes.

Here's an example of tax brackets in a certain tax system:

0 — 15,527: 0% tax

15,528 — 42,707: 15% tax

42,708 — 132,406: 25% tax

132,407 and more: 28% tax

Suppose we use a simplified version of taxation and apply one tax rate to the entire amount of money.

Write a program that calculates the tax that a person's going to pay based on their income.

The input format:

The value of someone's taxable income (in dollars).

The output format:

The tax for {income} is {percent}%. That is {calculated_tax} dollars!

Round your calculated_tax to the nearest integer.

Sample Input 1:

14378
Sample Output 1:

The tax for 14378 is 0%. That is 0 dollars!
Sample Input 2:

99999
Sample Output 2:

The tax for 99999 is 25%. That is 25000 dollars!
"""

def tax():
    income = int(input())
    if 0 <= income <= 15527:
        taxx = 0
    elif 15528 <= income <= 42707:
        taxx = 15
    elif 42708 <= income <= 132406:
        taxx = 25
    else:
        taxx = 28

    tot_tax = (income / 100) * taxx

    print(f'The tax for {income} is {taxx}%. That is {tot_tax :.0f} dollars!')


tax()
