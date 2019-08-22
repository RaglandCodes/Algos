'''

LeetCode 1021. Remove Outermost Parentheses
https://leetcode.com/problems/remove-outermost-parentheses/

'''
class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        ctr = 0
        a = ""
        for b in S:
            if b == "(":
                if ctr > 0:
                    a += "("
                
                ctr += 1
                
            else:
                if ctr != 1:
                    a += ")"
                
                ctr -= 1

        return a
            
            