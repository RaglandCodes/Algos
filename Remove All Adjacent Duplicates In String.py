'''

LeetCode 1047. Remove All Adjacent Duplicates In String
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/submissions/

'''
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        stack = []
        
        for s in S:
            if stack and stack[-1]==s:
                stack.pop()
            else:
                stack += [s]
            
        return "".join(stack)