"""
Indexes

Tail

Medium

Sentences generally end with a certain punctuation mark: a period ., an exclamation point !, or a question mark ?.

Find out which of these symbols marks the end of a string stored in the variable sentence and print it out

Sample Input 1:

What a lovely day!

Sample Output 1:

!
"""


sentence = input()

# now print the last symbol of `sentence`
n = len(sentence)
# print(n)
print(sentence[n - 1])