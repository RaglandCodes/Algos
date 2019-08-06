'''
LeetCode 485. Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones_count = 0
        max_count = 0
        for n in nums:
            if n == 1:
                ones_count += 1
            elif n != 1:
                max_count = max(max_count, ones_count)
                ones_count = 0
                
        return max(max_count, ones_count)
                
                