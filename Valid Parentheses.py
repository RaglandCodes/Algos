'''

LeetCode 20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/submissions/

'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        open_brackets = []
        
        for b in s:
            
            if b == '(':
                open_brackets.append('round')
            elif b == '[':
                open_brackets.append('square')
            elif b == '{':
                open_brackets.append('curly')
            
            elif b == ')':
                if not open_brackets: return False
                if open_brackets[-1] == 'round':
                    open_brackets.pop()
                else:
                    return False
                
            elif b == ']':
                if not open_brackets: return False
                if open_brackets[-1] == 'square':
                    open_brackets.pop()
                else:
                    return False
                
            elif b == '}':
                if not open_brackets: return False
                if open_brackets[-1] == 'curly':
                    open_brackets.pop()
                else:
                    return False
                
        if not open_brackets:
            return True
        return False
    