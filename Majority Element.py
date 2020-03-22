'''

LeetCode 169. Majority Element
https://leetcode.com/problems/majority-element/

Using the Boyer–Moore majority vote algorithm
https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm

'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = 0
        i = 0
        
        for n in nums:
            if i == 0:
                m = n
                i += 1
            elif m == n:
                i += 1
            else:
                i -= 1
        
        return m