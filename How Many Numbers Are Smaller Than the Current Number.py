'''

LeetCode 1365. How Many Numbers Are Smaller Than the Current Number
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

'''
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        a = [None] * len(nums)
        idx_d = {}
        
        for i, num in enumerate(nums):
            if num in idx_d:
                idx_d[num] += [i]
            else:
                idx_d[num] = [i]
            
        s = sorted(set(nums))
        
        smaller_count = 0
        
        for num in s:
            for i in idx_d[num]:
                a[i] = smaller_count
                
            smaller_count += len(idx_d[num])
        
        return a
                
        