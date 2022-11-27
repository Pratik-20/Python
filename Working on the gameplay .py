"""
Work on project. Stage 3/5: Working on the gameplay

Project: Last Pencil

Working on the gameplay

Description

An interesting idea has come to your mind. Let's change the rules of game. Players take turns taking X pencils until none of them remain.

Objectives
Expand your program by creating a loop. Each player takes turns removing pencils until 0 pencils remain on the table. Each iteration prints 2 lines: lines with pencils (vertical bars) and whose turn is now by printing the *NameX*'s turn string.

Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

How many pencils would you like to use:
> 5
Who will be the first (John, Jack):
> John
|||||
John's turn:
> 2
|||
Jack's turn:
> 1
||
John's turn:
> 2
Example 2:

How many pencils would you like to use:
> 15
Who will be the first (John, Jack):
> John
|||||||||||||||
John's turn:
> 8
|||||||
Jack's turn:
> 7
"""
def r():
    global pencils
    global player_one
    pencils = int(input('How many pencils would you like to use:'))
    player_one = input('Who will be the first (John, Jack)')
    #print(f'{player_one} is going first')
    print('|' * pencils)

def mm(pencils, counter = 1):
    while pencils > 0:
        #print("Counter is :", counter)
        player_one = ("John" if counter % 2 == 1 else "Jack")
        #print(player_one + "'s turn:")
        pen = int(input(player_one + "'s turn:"))
        counter = counter + 1
        pencils = pencils - pen
        print('|' * pencils)
def mmm(pencils, counter = 1):
    while pencils > 0:
        #print("Counter is :", counter)
        player_one = ("Jack" if counter % 2 == 1 else "John")
        #print(player_one + "'s turn:")
        pen = int(input(player_one + "'s turn:"))
        counter = counter + 1
        pencils = pencils - pen
        print('|' * pencils)
def re():
    if player_one == "John":
        mm(pencils)
    elif player_one == "Jack":
        mmm(pencils)
    else:
        print("Please enter correct Player name")

r()
re()
