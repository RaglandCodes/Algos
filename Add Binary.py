'''
LeetCode    67. Add Binary
https://leetcode.com/problems/add-binary/
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = list(a), list(b)
        
        len_a = len(a)
        len_b = len(b)
        len_diff = abs(len_a - len_b)
        if len_a < len_b:
            a = [0]*len_diff + a
        elif len_b < len_a:
            b = [0]*len_diff + b
        
        answer = ""
        carry = 0
        for i in range(1, len(a)+1):
            s = carry + int(a[-i]) + int(b[-i])
            if s == 0:
                answer = '0' + answer
                carry = 0
            elif s == 1:
                answer = '1' + answer
                carry = 0
            elif s == 2:
                carry = 1
                answer = '0' + answer
            elif s == 3:
                carry = 1
                answer = '1' + answer
        
        if carry == 1:
            answer = '1' + answer
        return answer  
        