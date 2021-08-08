"""
Task:
You have to create a program where a list of words is given and you have to print only those words which are longer than the given number n. N has to taken as input by the user.

Given_list = ["python" , "java" , "c" , "c++" , "kotlin"]

Input - 3

Output - ["python" , "java" , "kotlin"]
_____________________________________________
"""
list = ["python" , "java" , "c" , "c++" , "kotlin"]
list1=[]
print(list)
n = int(input())
a=len(list)
for i in range (a):	
	b= len(list[i])	
	if b>n:		
		list1.append((list[i]))
	else:
		("")
print(list1)