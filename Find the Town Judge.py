'''

LeetCode 997. Find the Town Judge
https://leetcode.com/problems/find-the-town-judge/

Solution from https://leetcode.com/problems/find-the-town-judge/discuss/242938/JavaC%2B%2BPython-Directed-Graph

'''
from collections import defaultdict

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        d = defaultdict(lambda: 0)
        
        if N == 1:
            return 1
        for t in trust:
            d[t[0]] -= 1
            d[t[1]] += 1
        
        print(d)
        for k, v in d.items():
            if v == N-1:
                return k
        
        
        
        return -1
            
        