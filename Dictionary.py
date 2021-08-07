"""
 
You have to create a program where you have to create a dictionary with key (1 to n) and value be square of the key.

Sample Run:-
input - 5
output - {1:1 , 2:4 , 3:9 , 4:16 , 5:25}

____________&______________________________
"""

dict = { }          # take a blank dictionary{}
n =int(input())  # take last degit as input

for i in range(n):    # Use For Loop
	i+=1                     # Set First no as 1
	a = i               
	b = a*a
	dict[a]=b
	
print(dict)        