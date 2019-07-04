'''
LeetCode 198. House Robber
https://leetcode.com/problems/house-robber/

Solution from https://www.youtube.com/watch?v=xlvhyfcoQa4
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        minus_two = nums[0]
        minus_one = max(nums[0], nums[1])
        minus_zero = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            minus_zero = max(nums[i] + minus_two, minus_one)
            minus_two, minus_one = minus_one, minus_zero
            
        return minus_zero
            