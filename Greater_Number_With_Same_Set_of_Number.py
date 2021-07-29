"""
Next Greater Number with Same Set of Digits

Given a number n, find the smallest number that has same set of digits as n and is greater than n. 

If n is the greatest possible number with its set of digits, then print “not possible”.

Examples:

(For simplicity of implementation, we have considered input number as a string.)

Input:  n = "1234"
Output: "1243"

Input: n = "4321"
Output: "Not Possible"

Input: n = "534976"
Output: "536479"

Topic : Arrays

Asked in Flipkart
"""

#__________________________________________#__________________________________________


#Take a Number as input
N = int(input("Please Enter a Number = "))
f = str(N)        # Convert int to string
b = (len(f))       # Lets Know length of Number

def Last_No():        # Create Function 
	list = [ ]                  # Create Blank list
	for n in range(b):      #Run for loop for b no.of times
	        a =(f[n])           #Access each element
	        t = (a)
	        list.append(t)    #Add element in list 
	        list.sort(reverse=True)     #Sort List elements in Decrese manner
	        s=""	       
	        s=s.join(list)      #Join elements of list
	        g= int(s)	# Convert String to int
	if g == N:
		print("Not Possible")
	else:
		print(g)     	
Last_No()



