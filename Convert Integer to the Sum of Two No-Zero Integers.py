'''

LeetCode 1317. Convert Integer to the Sum of Two No-Zero Integers
https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

'''
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        def noZero(num):
            # Maybe this is slower.
            #return str(num).count('0') == 0   
            
            
            while num>0:
                d = num%10
                if d == 0:
                    return False
                num = int(num/10)
            return True
        
        a = 1
        while True:
            if not noZero(a):
                a += 1
                continue
            b = n - a
            if noZero(b):
                return [a, b]
            
            a += 1
            
                