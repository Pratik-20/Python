n= int(input("Enter String size = "))

str1=input(str("Enter String = "))[:n]

print(str1)

for i in range (n):
	print(str1[i])
	
while(((str1[:1])!= ("+"))):
	print("Yes")
else:
	print("No")

