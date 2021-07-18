
list = [ ]         # Create a blank List

N = int(input("How much Elements You Want in List : "))       # How much elements you want in list
for i in range(N):
	i= int(input())      #Take Each element as input
	list.append(i)     #Add element in end of list
print(list)