'''
LeetCode 1089. Duplicate Zeros
https://leetcode.com/problems/duplicate-zeros/
'''
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        i = 0
        l = len(arr)
        
        while i < l:
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 2
                continue
            i += 1
        
        print(arr)