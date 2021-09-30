#Game Of Numbers

"""Aman and Jasbir are very intelligent guys of their batch. Today they are playing a game "Game of Numbers".

Description of game:

1.There are N numbers placed on a table.

2.Since two players are playing the game, they will make their moves alternatively.

3.In one move a player can perform the following operation.

a.A player will choose a number from the table and will replace that number with one of its divisor. For example, 6 can be replaced with 1, 2, or 3 (since these are the divisors of 6). Similarly, 12 can be replaced with 1, 2, 3, 4 or 6.

b.It is mandatory that the player has to replace the number. c.A player cannot put back the same number on table.

d.As 1 does not have any divisor other than itself, a player cannot replace 1 with any other number. So soon a situation will arise when there will be only all 1s on the table. In that situation the player will not be able to

make any move. The player who will not be able to make the move, loses.

4.Both the players are masters of this game. So they will play the game optimally. 5.Aman will make the first move of the game.

You will be given N integers that are on the table. You have to predict, who will win the game - Aman or Jasbir.
"""



n= int(input())

lst=[ ]

lst= list(map(int,input(""). strip(). split()))[:n]

print(lst[:n])

sum = 0
for i in range (len(lst)):
	sum= sum^lst[i]


if(sum==0):
	print("Jasbir")
	
else:
    print("Aman")
	



