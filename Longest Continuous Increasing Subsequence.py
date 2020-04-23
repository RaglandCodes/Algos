'''

LeetCode 674. Longest Continuous Increasing Subsequence
https://leetcode.com/problems/longest-continuous-increasing-subsequence/submissions/

'''
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        if nums == []:
            return 0
        
        mc = 1  # max count
        cc = 1  # current count
        
        for i, n in enumerate(nums):
            if i == 0:
                continue
            
            if n > nums[i-1]:
                cc += 1
            else:
                cc = 1
            
            if cc > mc:
                mc = cc
        
        return mc
            
            
            