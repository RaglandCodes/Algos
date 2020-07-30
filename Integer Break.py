'''

LeetCode 343. Integer Break
https://leetcode.com/problems/integer-break/

'''
from collections import defaultdict 
class Solution:
    def integerBreak(self, n: int) -> int:
        cache = defaultdict(lambda: 0)
        if n == 3:
            return 2
        
        def getAns(num):
            if num < 3:
                return 1
            
            if cache[num] > 0:
                return cache[num]
            
            max_val = 1
            for i in range(1, num+1):
                max_val = max(max_val, i * getAns(num-i))
            
            cache[num] = max_val
            
            return max_val
        
        return(getAns(n))
        