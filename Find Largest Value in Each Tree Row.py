'''

LeetCode 515. Find Largest Value in Each Tree Row
https://leetcode.com/problems/find-largest-value-in-each-tree-row/

'''
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        a = []
        
        if not root:
            return a
        
        cur_q = deque()
        next_q = deque()
        
        cur_q.append(root)
        cur_max = None
        
        while True:
            node = cur_q.popleft()
            
            if cur_max is None:
                cur_max = node.val
            elif node.val > cur_max:
                cur_max = node.val
                
            if node.right:
                next_q.append(node.right)
                
            if node.left:
                next_q.append(node.left)
            
            if not cur_q:
                a.append(cur_max)
                if not next_q:
                    break
                
                cur_max = None
                cur_q = next_q
                next_q = deque()
        
        
        return a