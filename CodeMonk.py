t=int(raw_input())
while t !=0:
	n= int( raw_input())
	arr=(int,raw_input().split(" "))
	arr.sort()
	min = arr[0]^arr[1]
	for i in range(1,n-1):
		temp= arr[i] ^ arr[i+1]
		if temp<min:
			min = temp
	print min
	print " "
	t-=1