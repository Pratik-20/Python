"""
Work on project. Stage 4/5: Fair play
Project: Last Pencil

Fair play

Hard

Description

The game was interesting, but it went sour. No one was playing a fair game! You've taken 10 pencils, your friend decided that it is unfair and somehow took a negative number! Moreover, you both can't decide which of you won. Maybe, it's time to add new rules to the game?

Objectives
In this stage, your task is to add a new level of control over the game. Check the input. If it's incorrect, print the reason why. Also, limit the possible amount of pencils taken. Let's say that players can remove not more than 3 pencils at a time.

Here are possible errors and their feedback:

The initial number of pencils is not a numeric string, so it can't be converted to an integer — The number of pencils should be numeric;
The initial number of pencils is equal to 0 — The number of pencils should be positive;
If the input is a negative amount, apply condition (1), as the minus sign is not a numeric;
If the chosen first player is not *Name1* or *Name2* — Choose between *Name1* and *Name2*;
One of the players has taken the number of pencils that differs from 1, 2, or 3 — Possible values: '1', '2' or '3';
One of the players has taken more pencils than there are on the table — Too many pencils were taken.
If one of the errors occurs, ask for input once again.

Don't forget to help determine the winner of the game. The player who takes the last pencil loses the game. Print out the result at the end of the game with the line *Winner-name* won!

Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1: the initial number of pencils is not numeric

How many pencils would you like to use:
> a
The number of pencils should be numeric
> 5
Who will be the first (John, Jack):
>
Example 2: the initial number of pencils equals 0

How many pencils would you like to use:
> 0
The number of pencils should be positive
> 20
Who will be the first (John, Jack):
>
Example 3: the chosen first player is not in the list

How many pencils would you like to use:
> 5
Who will be the first (John, Jack):
> JohnJack
Choose between 'John' and 'Jack'
> John
|||||
John's turn!
>
Example 4: one of the players has taken the number of pencils that differs from 1, 2, or 3

How many pencils would you like to use:
> 5
Who will be the first (John, Jack):
> John
|||||
John's turn!
> 4
Possible values: '1', '2' or '3'
> 1
||||
Jack's turn!
>
Example 5: the chosen number of pencils is not numeric

How many pencils would you like to use:
> 5
Who will be the first (John, Jack):
> John
|||||
John's turn!
> a
Possible values: '1', '2' or '3'
> 1
||||
Jack's turn!
>
Example 6: John is the winner of the game

How many pencils would you like to use:
> 5
Who will be the first (John, Jack):
> John
|||||
John's turn!
> 3
||
Jack's turn!
> 3
Too many pencils were taken
> 2
John won!

"""

def choose():
    global pencils
    PV = ["1", "2", "3"]
    name_list = ['John', 'Jack']
    print("Who will be the first (John, Jack):")
    name = input()
    while name not in name_list:
        print("Choose between 'John' and 'Jack'")
        name = input()
    while int(pencils) > 0:
        print('|' * int(pencils))
        print(f"{name}'s turn:")
        removed = input()
        while removed not in PV:
            print("Possible values: '1', '2' or '3'")
            removed = input()

        while int(removed) > pencils :
            print("Too many pencils were taken")
            removed = input()

        pencils -= int(removed)
        name = 'Jack' if name == 'John' else 'John'
    last_name = name
    if last_name == 'Jack':
        print("Jack won!")
    else:
        print("John won!")


def numb():
    global pencils

    pencils = input()
    while not pencils.isdigit():
        print("The number of pencils should be numeric")
        numb()
    pencils = int(pencils)
    while not int(pencils) > 0:
        print("The number of pencils should be positive")
        numb()
    choose()


print('How many pencils would you like to use:')
numb()