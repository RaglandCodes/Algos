'''

Leetcode 338. Counting Bits
https://leetcode.com/problems/counting-bits/

This is faster than only 5% of the Python3 submissions.
Could be made faster using memoization to prevent repetitions maybe.

'''
class Solution:
    def countBits(self, num: int) -> List[int]:
        a = []
        
        for i in range(0, num+1):
            n = i        
            this_a = 0
            while n > 0:
                mul2 = 1
                while (mul2*2) <= n:
                    mul2 *= 2
                n -= mul2
                this_a += 1
            
            a += [this_a]
        
        return a
                
                