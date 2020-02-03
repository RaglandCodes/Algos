'''

LeetCode 1313. Decompress Run-Length Encoded List
https://leetcode.com/problems/decompress-run-length-encoded-list/

'''
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        o = []
        
        for i in range(0, len(nums), 2):
            o += [nums[i+1] for j in range(nums[i])]
        
        return o
    