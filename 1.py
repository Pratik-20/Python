"""
Task:
You have to create a program where you have to create a list of first 5 and last 5 numbers in range of number 1 to 30.

______________________________________________________________________________________"""

List= [ ]
i = 0
j= 0
a = 1#int(input("Enter First Number:- "))
b = 30#int(input("Enter First Number:- "))

List.append(a)
for i in range(4):
	a=a+1
	#print(a)
	List.append(a)
List.append(b)
for j in range(4):
	b=b-1
	#print(b)
	List.append(b)

print(List)		