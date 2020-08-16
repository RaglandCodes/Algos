'''

LeetCode 93. Restore IP Addresses
https://leetcode.com/problems/restore-ip-addresses/

a, b and c are position of the points
Just move them around and check if the numbers between the points are valid

The if len_n > 3: check is an attempt to reduce str -> int conversions

'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        
        a = 1
        b = 2
        c = 3
        
        l = len(s)
        def isValid(n):
            len_n = len(n)
            if len_n == 0 or len_n > 3:
                return False

            if n[0] == '0' and len_n > 1:
                return False
            
            return int(n) <= 255
        
        ans = []
        
        for i in range(c, l):
            if not isValid(s[i:]):
                continue
            for j in range(b, l):
                if not isValid(s[j:i]):
                    continue
                for k in range(a, l):
                    if isValid(s[k:j]) and isValid(s[:k]):
                        ans.append(s[:k] + "." +s[k:j]+"."+ s[j:i]+ "."+ s[i:])
                        
        return ans
    