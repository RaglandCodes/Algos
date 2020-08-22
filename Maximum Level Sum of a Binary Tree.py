'''

1161. Maximum Level Sum of a Binary Tree
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

'''
from collections import deque 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        curr_q = deque() 
        next_q = deque()
        
        curr_q.append(root)
        
        max_sum = root.val
        cur_sum = 0
        
        cur_lvl = 1
        max_lvl = 1
        
        while curr_q or next_q:
            if not curr_q:
                curr_q, next_q = next_q, deque()
                if cur_sum > max_sum:
                    max_sum = cur_sum
                    max_lvl = cur_lvl
                cur_sum = 0
                cur_lvl += 1
                    
                max_sum = max(max_sum, cur_sum)
                
            
            node = curr_q.popleft()
            if node is None:
                continue
            cur_sum += node.val
            
            next_q.append(node.left)
            next_q.append(node.right)
            
        return max_lvl