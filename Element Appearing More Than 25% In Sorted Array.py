'''

LeetCode 1287. Element Appearing More Than 25% In Sorted Array
https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

'''
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        mc = 0  #max count
        cc = 0  #current count
        mn = arr[0]     #max number
        ce = arr[0]
        for i, n in enumerate(arr):
            if arr[i] == ce:
                cc += 1
            else:
                cc = 1
                ce = n
            if cc > mc:
                mc = cc
                mn = n
            
            
            
        return mn