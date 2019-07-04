'''
https://leetcode.com/problems/maximum-subarray

Solved using Kadane\'s Algorithm
https://www.youtube.com/watch?v=86CQq3pKSUw
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        thisSum = nums[0]
        for i in range(1, len(nums)):
            if(nums[i] > thisSum+nums[i]):
                thisSum = nums[i]
            else:
                thisSum += nums[i]
            if(thisSum > maxSum):
                maxSum = thisSum
        return(maxSum)
