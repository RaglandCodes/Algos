'''

LeetCode 1266. Minimum Time Visiting All Points
https://leetcode.com/problems/minimum-time-visiting-all-points/

This could be made faster by not taking just one step in each iteration. 
Now it's only faster than 5% of Python3 online submissions 😢

'''
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        p = points[0]
        a = 0
        for point in points:
            while p != point:
                if p[0] == point[0]:
                    if p[1] < point[1]:
                        p[1] += 1
                        a += 1
                    else:
                        p[1] -= 1
                        a += 1
                
                elif p[1] == point[1]:
                    if p[0] < point[0]:
                        p[0] += 1
                        a += 1
                    else:
                        p[0] -= 1
                        a += 1
                else:
                    if p[0]< point[0]:
                        if p[1] < point[1]:
                            p[0] += 1
                            p[1] += 1
                        else:
                            p[0] += 1
                            p[1] -= 1
                    else:
                        if p[1] < point[1]:
                            p[0] -= 1
                            p[1] += 1
                        else:
                            p[0] -= 1
                            p[1] -= 1
                            
                    a += 1
        
        return a