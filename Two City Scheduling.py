'''
LeetCode 1029. Two City Scheduling
https://leetcode.com/problems/two-city-scheduling/

Answers from here ⬇ 
- https://www.youtube.com/watch?v=OkJ1aHjAQr8
- https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/
- https://stackoverflow.com/questions/4183506/python-list-sort-in-descending-order
'''
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ctr_a = 0
        ctr_b = 0
        a = 0
        n = len(costs)
        
        for i, c in enumerate(costs):
            costs[i].append(abs(costs[i][0] - costs[i][1]))
            
        # costs = sorted(costs, key = lambda x: x[2])[::-1]
        
        costs = sorted(costs, key = lambda x: x[2], reverse=True)
        
        for i, c in enumerate(costs):
            if ctr_a < n and ctr_b < n:
                if costs[i][0] < costs[i][1]:
                    ctr_a += 2
                    a += costs[i][0]
                elif costs[i][1] < costs[i][0]:
                    ctr_b += 2
                    a += costs[i][1]
                    
            elif ctr_a < n:
                ctr_a += 2
                a += costs[i][0]
            
            else:
                ctr_b += 2
                a += costs[i][1]
                
        return a
        