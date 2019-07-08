'''
LeetCode | 944. Delete Columns to Make Sorted
https://leetcode.com/problems/delete-columns-to-make-sorted/
'''
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        a = 0
        for i in range(len(A[0])):
            for j in range(1, len(A)):
                if(A[j][i] < A[j-1][i]):
                    a += 1
                    break
                
        return a
            