'''

LeetCode 739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/


Got answer from https://leetcode.com/problems/daily-temperatures/discuss/109867/Simple-Python-stack-solution/113938
'''
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        length = len(T)
        a = [0] * length
        stack = []
        
        for i in range(length-1, -1, -1):
            while stack and stack[-1][0] <= T[i]:
                stack.pop()
            
            if stack:
                a[i] = stack[-1][1] - i
            
            stack += [[T[i], i]]
            
        
        return a
                