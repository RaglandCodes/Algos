'''

LeetCode 392. Is Subsequence
https://leetcode.com/problems/is-subsequence/

'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        
        i = 0
        j = 0
        f = 0       # found
        while i<m:
            while j<n:
                if t[j] == s[i]:
                    f += 1
                    j += 1
                    break
                j += 1
            i += 1
            
        if f == m:
            return True
        return False
        