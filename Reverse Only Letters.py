'''
LeetCode 917. Reverse Only Letters
https://leetcode.com/problems/reverse-only-letters/
'''
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:

        letters = ""
        for s in S:
            if (s>='a' and s<='z') or (s>='A' and s<='Z'):
                letters += s
            
        letters = letters[::-1]
        for i, s in enumerate(S):
            if not((s>='a' and s<='z') or (s>='A' and s<='Z')):
                letters = letters[:i] + s + letters[i:]
        
        return letters
    