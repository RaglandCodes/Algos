'''

LeetCode 1302. Deepest Leaves Sum
https://leetcode.com/problems/deepest-leaves-sum/

'''
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        cur_q =deque()
        next_q =deque()
        
        cur_q.append(root)
        cur_sum = 0
        
        while cur_q or next_q:
            if not cur_q:
                cur_q, next_q = next_q, cur_q
                cur_sum = 0
            
            node = cur_q.popleft()
            
            
            if node.left:
                next_q.append(node.left)
            if node.right:
                next_q.append(node.right)
            elif not node.left:
                #leaf node, add node.val only when in leaf node
                cur_sum += node.val
                
                
        
        return cur_sum
                    
            
        