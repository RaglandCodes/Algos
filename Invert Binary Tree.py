'''

LeetCode 226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

'''

from collections import deque 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        print(root)
        q = deque([root])
        
        while q:
            if q[0] is None:
                q.popleft()
                continue
                
            if q[0].right is None and q[0].left is None:
                q.popleft()
                continue
                
            q[0].left, q[0].right = q[0].right, q[0].left
            q.append(q[0].left)
            q.append(q[0].right)
            
            q.popleft()
        
        return root
            
            