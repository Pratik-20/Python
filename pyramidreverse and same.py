n = int(input(print("Enter vlue of n")))


def pattern(n):
	for j in range (0,n):
		for i in range (0, j+1):
			print("*", end ="")
		print("\r")
pattern(n)	


def revers(n):
	for i in range(0,n):
		for i in range(0,n-i):
			print("*",end="")
		print("\r")
revers(n)
	
	
	
	
	