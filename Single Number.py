'''

Leetcode 136. Single Number 
https://leetcode.com/problems/single-number/submissions/

This code uses the fact the
x^0s = x
x^x = 0


The commented method doesn't use bit manipulation

'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums[0]
        
        for i in range(1, len(nums)):
            a ^= nums[i]
            
        return a
        
#         if len(nums) == 1:
#             return nums[0]
        
#         nums = sorted(nums)
#         i = 0
        
#         if nums[-1] != nums[-2]:
#             return nums[-1]
        
#         while i < len(nums)-1:
#             if nums[i] == nums[i+1]:
#                 i += 2
#             else:
#                 return nums[i]
                