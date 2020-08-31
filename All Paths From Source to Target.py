'''

LeetCode 797. All Paths From Source to Target
https://leetcode.com/problems/all-paths-from-source-to-target/

'''
from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph) - 1
        paths = []
        q = deque()
        
        for p in graph[0]:
            if p == N:
                paths.append([0,p])
            else:
                q.append([0, p])
            
        while q:
            next_path = q.popleft()
            for n in graph[next_path[-1]]:
                new_path = next_path + [n]
                if n == N:
                    paths.append(new_path)
                else:
                    q.append(new_path)
                
        return paths
            
        