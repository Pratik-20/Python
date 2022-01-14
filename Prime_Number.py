n= int(input())
b=0
a = int(n/2)

for i in range(2,a-2):
	if (n%i==0):
		print("This is Non Prime Number")
		b=1
	break
if (b==0):
	print("Prime Number")