import random 
t = ["Snake","Water","Gun"]
print("Enter Your Choice as 1,2,3 where 1 for Snake🐍,2 for Water🥛, 3 for Gun🏹")
a=0
b=0
#print("Score: ")
for i in range (10):
    i+=1
    print(i)
    y= random.choice(t)
    #print(y)
    s = int(input("Enter Your Choice: "))
    if (y==(t[1])and (s == 1)):
	    #print("You Won")
	    a+=1
    elif (y==(t[0])and (s==3)):
    	#print("You Won")
    	a+=1				
    else:
	    #	print("You Lost")
	    b+=1
print("Your Score",a)
print("Computer's Score",b)
if(a>b):
	print("You Win😀")
elif(b>a):
	print("You Lost😩")
elif(b==a):
	print("Same Sore..🤣")
else:
	print("Sorry Something Went Wrong😌")