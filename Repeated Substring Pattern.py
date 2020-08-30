'''

LeetCode 459. Repeated Substring Pattern
https://leetcode.com/problems/repeated-substring-pattern/

'''
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        
        def check(ls):
            if s[:ls] * (l // ls) == s:
                return True
        
        if l <= 1:
            return False
        
        if check(1):
            return True
        
        for i in range(2, int(l**0.5)+1 ):
            if len(s) % i == 0: 
                if check(i):
                    return True
                if check(l // i):
                    return True
        
        return False