'''

LeetCode 1003. Check If Word Is Valid After Substitutions
https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

This is something like the array open/close logic, but one more intermediate step i.e. b

'''
class Solution:
    def isValid(self, S: str) -> bool:
        open_stack = []
        
        for l in S:
            if l == "a":
                open_stack += ['a']
            elif l == "b":
                if not open_stack:
                    return False
                if open_stack[-1] == "a":
                    open_stack[-1] = "ab"
                else:
                    return False
            else:
                if not open_stack:
                    return False
                if open_stack[-1] == "ab":
                    open_stack.pop()
                else:
                    return False
        
        if not open_stack:
            return True
        return False
        
                    