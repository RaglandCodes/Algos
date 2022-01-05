'''

LeetCode 11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Solution from
https://www.code-recipe.com/post/container-with-most-water

'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        
        this_vol = min(height[left], height[right]) * (right - left)
        most_vol = this_vol
        
        
        while left < right:
            this_vol = min(height[left], height[right]) * (right-left)
            
            most_vol = max(this_vol, most_vol)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
                
            
            
        return max(most_vol, this_vol)