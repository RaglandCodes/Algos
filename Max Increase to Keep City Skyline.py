'''

LeetCode 807. Max Increase to Keep City Skyline
https://leetcode.com/problems/max-increase-to-keep-city-skyline/

'''

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        left_skyline = [0]* len(grid) # = right_skyline
        top_skyline = [0]*len(grid[0])
        
        for i, row in enumerate(grid):
            for j, building in enumerate(row):
                if building > left_skyline[i]:
                    left_skyline[i] = building
                    
                if building > top_skyline[j]:
                    top_skyline[j] = building
                    
        
        a = 0        
        for i, row in enumerate(grid):
            for j, building in enumerate(row):
                maxx = min(left_skyline[i], top_skyline[j])
                if maxx > building:
                    a += (maxx - building)
                
        return a