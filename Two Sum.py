'''

LeetCode 1. Two Sum
https://leetcode.com/problems/two-sum/

The O(N^2) answer is commented.

Got the O(N) answer from 
https://leetcode.com/problems/two-sum/discuss/17/Here-is-a-Python-solution-in-O(n)-time

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        
        for i in range(len(nums)):
            if nums[i] not in d:
                d[target - nums[i]] = i
            else:
                return [i, d[nums[i]]]
        
                
#         l = len(nums)
        
#         for i in range(l):
#             for j in range(i+1, l):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
            
        
        
        