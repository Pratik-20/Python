n= int(input())

#i= 0
def pyr(n):
       for i in range(0,n):
             for j in range (0,i+1):
                 	print("*",end= "")
             print("\r")

pyr(n)