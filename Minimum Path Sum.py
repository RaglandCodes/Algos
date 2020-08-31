'''

LeetCode 64. Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum/submissions/

Slow TLE approach https://leetcode.com/submissions/detail/388851332/

'''
from collections import deque
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j-1]
                    continue
                if j == 0:
                    grid[i][j] += grid[i-1][j]
                    continue
                grid[i][j] += min(grid[i][j-1], grid[i-1][j])
                
        return grid[-1][-1]
                    