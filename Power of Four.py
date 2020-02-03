'''

LeetCode 342. Power of Four
https://leetcode.com/problems/power-of-four/

'''

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        
        binary = list(bin(num)[2:])
        
        if(binary[0] == '1' and (list(set(binary[1:])) == ['0'] or list(set(binary[1:])) == [] )and len(binary[1:])%2 == 0):
            return True
        return False
    
    
    '''
    
    list(set(binary[1:])) ==  [] handles case when input is 1
    '''
        