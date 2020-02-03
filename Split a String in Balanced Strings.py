'''

LeetCode 1221. Split a String in Balanced Strings
https://leetcode.com/problems/split-a-string-in-balanced-strings/

'''
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        a = 0 
        current = []
        for letter in s:
            current += letter
            if current.count('L') == current.count('R'):
                current = []
                a += 1
        return a
        