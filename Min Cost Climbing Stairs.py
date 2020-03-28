'''

LeetCode 746. Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/

'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        
        if n < 2:
            return 0
        
        a, b = cost[0], cost[1]
        
        for i in range(2, n):
            a, b = b, min(a, b) + cost[i]
        
        return min(a, b)
        
