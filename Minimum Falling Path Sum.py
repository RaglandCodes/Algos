'''

LeetCode 931. Minimum Falling Path Sum
https://leetcode.com/problems/minimum-falling-path-sum/

'''
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        
        n = len(A)
        for i in range(n-2, -1, -1):
            for j in range(n):
                if j == 0:
                    A[i][j] += min([A[i+1][j], A[i+1][j+1]])
                elif j+1 == n:
                    A[i][j] += min([A[i+1][j], A[i+1][j-1]])
                else:
                    A[i][j] += min([A[i+1][j-1], A[i+1][j], A[i+1][j+1]])
            
        return min(A[0])
                    
            