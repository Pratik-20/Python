t= int(input())
while t!=0:
	n= int(input("Enter String size = "))
str1=input(str("Enter String = "))[:n]
flag= 0

while (((str1[:1])!= ("+"))):
		print("No")
				
for i in range (n):
	s1=str1[i:i+3]	
	if((s1)==("HHH")):
	   print("No")	   
	   flag =1
	   break	

if(flag != 1):
		print("Yes")
t-=1