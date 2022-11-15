"""
How many nuts will be left after division

Some squirrels found some nuts and decided to divide them equally.
You will get the number of squirrels and the number of nuts as input on separate lines.
Find out how many nuts will be left after each of the squirrels takes an equal number of nuts.
Print the result.


Sample Input 1:
3
14

Sample Output 1:
2

"""
n = int(input())
m = int(input())

print(int(m % n))