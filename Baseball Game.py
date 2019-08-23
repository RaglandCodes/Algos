'''

LeetCode 682. Baseball Game
https://leetcode.com/problems/baseball-game/submissions/

'''
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        
        for op in ops:
            if op=='C':
                stack.pop()
            elif op=='D':
                stack.append(2 * stack[-1])
            elif op=='+':
                stack.append(stack[-2] + stack[-1])
            else:
                stack.append(int(op))
        
        return sum(stack)
        