'''

LeetCode 1249. Minimum Remove to Make Valid Parentheses
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_stack = []
        a = ""
        for i, letter in enumerate(s):
            if letter == "(":
                open_stack += [len(a)]
                a += letter
            elif letter == ")":
                if len(open_stack) > 0:
                    open_stack.pop()
                    a += letter
            else:
                a += letter
        
        if len(open_stack) == 0:
            return a
        
        aa = ""
        for i, letter in enumerate(a):
            if letter == "(":
                if i in open_stack:
                    continue
            aa += letter
            
        return aa
    