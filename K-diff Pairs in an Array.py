'''

LeetCode 532. K-diff Pairs in an Array
https://leetcode.com/problems/k-diff-pairs-in-an-array/

Sorting and comparing gives TLE https://leetcode.com/submissions/detail/315098529/
Even this method is slow 😢 (Faster than 5%). I think the problem is that I'm doing to `in` checks (h and used).

'''
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        h = []
        a = 0
        if k<0:
            return 0
        used = []   #[[smaller, bigger]]
        for n in nums:
            minus = n - k
            plus = n + k
            if minus in h and [minus, n] not in used:
                a += 1
                used.append([minus, n])
            if plus in h and [n, plus] not in used:
                a += 1
                used.append([n, plus])
            h.append(n)             
        return a
            
        
                    
                
        
        