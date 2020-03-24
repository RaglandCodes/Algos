'''

LeetCode 215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Heap docs https://docs.python.org/3/library/heapq.html


'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        return (heapq.nlargest(k, nums, key=None))[-1]
        
        #return sorted(nums, reverse=True)[k-1]