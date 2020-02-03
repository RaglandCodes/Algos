'''

LeetCode 520. Detect Capital
https://leetcode.com/problems/detect-capital/

'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word: 
            return True
        if word.lower() == word: 
            return True
        if word[0].upper() == word[0] and word[1:] == word[1:].lower():
            return True
        
        return False