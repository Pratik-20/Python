"""
Indexes

Lucky ticket

Hard

Lucky tickets are a kind of mathematical entertainment. A ticket is considered lucky if the sum of the first 3 digits equals the sum of the last 3 digits of the ticket number.
You are supposed to write a program that checks whether the two sums are equal. The code snippet below displays "Lucky" if they are and "Ordinary" if they are not.

However, some parts of the code are missing. Fill in the blanks to make it work!

Input: a string of 6 digits.

Output: either "Lucky" or "Ordinary" (without quotes).

Make sure that you are NOT concatenating strings. To do this, convert each digit in the ticket number to an integer. Don't forget to use proper indices.



Sample Input 1:

090234
Sample Output 1:

Lucky
Sample Input 2:

123456
Sample Output 2:

Ordinary

"""

# Save the input in this variable
ticket = input()

# Add up the digits for each half
half_1 = [int(ticket[0]) + int(ticket[1]) + int(ticket[2])]
half_2 = [int(ticket[3]) + int(ticket[4]) + int(ticket[5])]

# Thanks to you, this code will work
if half_1 == half_2:
    print("Lucky")
else:
    print("Ordinary")
