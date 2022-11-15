"""
Longest word

Medium

Find the longest word in a pair and print its length.

The variables word1 and word2 are defined for you.

Sample Input 1:

Riddikulus
Alohomora

Sample Output 1:

10

Sample Input 2:

earthquake
Supercalifragilisticexpialidocious
Sample Output 2:

34

"""


word1 = input()
word2 = input()

# How many letters does the longest word contain?
#x = len(word1)
#y = len(word2)

if (len(word1)>=len(word2)):
    print(len(word1))
else:
    print(len(word2))