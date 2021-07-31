"""
Task:
You have to create a program where a list of numbers is given and a number of rotation is given. Now you to bring last number of list in front and swift each number to the right. Do this till the given number of rotation.

Sample :-
input - [1,2,3,4] , 2
output - [3,4,1,2] 
______________________________________________________________________________________
"""
#algorithm
x = list(map(int, input("Enter a multiple value: ").split()))
print("List of students: ", x)
j = int(input())
b= (len(x))
for i in range(j):
	a = x[b-1]
	x.insert(0,a)
	x.pop()
print(x)
