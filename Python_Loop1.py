"""
DESCRIPTION
Complete the DecimalToBinary function with appropriate code to
accept an integer in the range 1 to 999 and display the binary
equivalent of that number as output.


Following requirements should be taken care in the program.
Input should be taken through Console


If the number is less than 1 or greater than 999 then the output should show as "INVALID_INPUT"
Use While loop to solve the above problem.
Complete below given function -

decimalTobinary(num)

Sample Input 1:
10
Expected Output 1:
1010


Sample Input 5:
457
Expected Output 5:
111001001

EXECUTION TIME LIMIT
10 seconds

"""
def de(decimal):
    """
    if(num < 1):
        print("INVALID_INPUT")
    elif(num > 999):
        print("INVALID_INPUT")
    """
    while (num < 1 or num >999):
        print("INVALID_INPUT")
        break

    else:
        if (decimal > 0):
            de((int)(decimal / 2))
            print(decimal % 2, end='')


num = int(input())
decimal = num
de(decimal)