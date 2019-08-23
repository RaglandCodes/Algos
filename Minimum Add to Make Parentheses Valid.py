'''

LeetCode 921. Minimum Add to Make Parentheses Valid
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

'''
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        o = 0
        a = 0
        
        for s in S:
            if s == ')':
                if o == 0:
                    a += 1
                else:
                    o -= 1
            else:
                o += 1
        
        return a+o