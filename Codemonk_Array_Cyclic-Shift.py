#Codemonk "©yclic Shift"

t = int( input())
while t!=0 :
	n,k= map(int, input().split())
	s= raw_input()
	max= " "
	p= -1
	for i in range (n):
		if max < s:
			max=s
			d=i
		elif max==s:
			p=i-d
			break
		s=s[1:]+s[:1]
	if p==-1:
		print(d+(k-1)*n)
	else:
		print(d+(k-1)*p)
	print("") 
	t-=1