"""
Arguments

Misfortune

Robin has declared a function that prints the squares of odd numbers in the specified range. Unfortunately, several function calls gave an unexpected result. The function itself seems to be fine. Help Robin figure out what went wrong in these calls and fix them.

For each case, the required range is written in a comment.


"""


# the function is fine, you do not need to change it
def square_odds(a, b):
    start = a
    if a % 2 == 0:
        start += 1
    end = b + 1
    for odd in range(start, end, 2):
        print(odd ** 2)


# from 22 to 42
square_odds(22, 42)

# from 15 to 31
square_odds(15, 31)

# from 42 to 49
square_odds(b=49, a=42)
