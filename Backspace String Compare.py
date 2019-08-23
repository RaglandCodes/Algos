'''

LeetCode 844. Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/submissions/

'''
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        stack_s = []
        stack_t = []
        
        for s in S:
            if s == '#':
                if stack_s:
                    stack_s.pop()
            else:
                stack_s += [s]
        
        for s in T:
            if s == '#':
                if stack_t:
                    stack_t.pop()
            else:
                stack_t += [s]
        
        return stack_t == stack_s
                