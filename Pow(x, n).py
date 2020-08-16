'''

LeetCode 50. Pow(x, n)
https://leetcode.com/problems/powx-n/

'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(xx, nn):
            if nn == 0:
                return 1
            if nn == 1:
                return x
            
            if nn%2 == 0:
                t = power(xx, nn/2)
                return t * t
            else:
                t = power(xx, int(nn/2))
                return xx * t * t
        
        neg = n < 0
        a = power(x, abs(n))
        
        if neg:
            return 1/a
        
        return a
        
        
        
        
        
        
        
        