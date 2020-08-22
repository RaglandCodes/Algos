'''

LeetCode 104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

'''
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        cur_level = deque()
        next_level = deque()
        cur_level.append(root)
        
        a = 1
        
        while cur_level or next_level:
            if not cur_level:
                a += 1
                cur_level, next_level = next_level, cur_level
                
            node = cur_level.popleft()
            if node.right:
                next_level.append(node.right)
                
            if node.left:
                next_level.append(node.left)
                
        return a
                
        