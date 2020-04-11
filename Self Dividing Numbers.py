'''

LeetCode 728. Self Dividing Numbers
https://leetcode.com/problems/self-dividing-numbers/

'''
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDividing(n):
            on = n          #original n
            if n<10:
                return True
            while n>0:
                digit = n%10
                if digit == 0:
                    return False
                if on % digit > 0:
                    return False
                n = int(n/ 10)
            return True
                    
        a = []
        
        for i in range(left, right + 1):
            if(isSelfDividing(i)):
                a += [i]
                
        return a;