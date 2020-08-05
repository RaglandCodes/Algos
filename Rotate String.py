'''

796. Rotate String
https://leetcode.com/problems/rotate-string/

'''
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        
        if len(A) != len(B):
            return False
        
        
        left_done = False
        current = ''
        
        for c in A:
            current += c
            
            if current in B:
                continue
            
            if left_done:
                return False
            
            left_done = True
            current = c
        
        return True
            
                
            
            