"""
1347. Minimum Number of Steps to Make Two Strings Anagram

You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Example
1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace
the
first
'a' in t
with b, t = "bba" which is anagram of s.
Example
2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace
'p', 'r', 'a', 'i' and 'c'
from t

with proper characters to make t anagram of s.
Example
3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar"
are
anagrams.

Constraints:

1 <= s.length <= 5 * 104
s.length == t.length

s and t consist of lowercase English letters only.
"""

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # initialize two arrays to store the frequency of each character in s and t
        count_s = [0] * 26
        count_t = [0] * 26

        # loop through the characters in s and increment the corresponding frequency in count_s
        for char in s:
            # subtract the ASCII value of 'a' from the ASCII value of the character to get the index of the array
            count_s[ord(char) - ord('a')] += 1

        # loop through the characters in t and increment the corresponding frequency in count_t
        for char in t:
            # subtract the ASCII value of 'a' from the ASCII value of the character to get the index of the array
            count_t[ord(char) - ord('a')] += 1

        # initialize the number of steps to 0
        steps = 0
        # loop through the 26 possible characters
        for i in range(26):
            # add the absolute difference between the frequencies in count_s and count_t to the number of steps
            steps += abs(count_s[i] - count_t[i])

        # return the number of steps divided by 2, since each step can change two characters
        return steps // 2
