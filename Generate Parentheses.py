'''

LeetCode 22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/

'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        a = []
        
        n2 = n*2
        
        def gen(p, l, r):
            nonlocal a
        
            if len(p) == n2:
                a.append(p)
            if l < n:
                gen(p+"(", l+1, r)
            if r<l:
                gen(p+")",l, r+1 )
        
        
            
        gen("", 0, 0)
        return a