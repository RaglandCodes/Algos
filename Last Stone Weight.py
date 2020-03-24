'''
LeetCode 1046. Last Stone Weight
https://leetcode.com/problems/last-stone-weight/

Python heap

docs https://docs.python.org/3/library/heapq.html
tutorial https://www.tutorialspoint.com/python_data_structure/python_heaps.htm

'''
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = list(map(lambda x: 0-x, stones))
        heapq.heapify(stones)
        
        while stones:
            a = heapq.heappop(stones)
            if not stones:
                return 0 - a
                
            b = heapq.heappop(stones)
            heapq.heappush(stones, a - b)
            heapq.heapify(stones)
