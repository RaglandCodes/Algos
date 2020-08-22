'''

LeetCode 112. Path Sum
https://leetcode.com/problems/path-sum/

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root:
            return False
        
        if (not root.left) and (not root.right):
            # leaf node
            return root.val == sum
        
        if root.left and root.right:
            if self.hasPathSum(root.left, sum-root.val):
                return True
            
            # check the right path only if left path is not possible for answer
            return self.hasPathSum(root.right, sum - root.val)
        
        if root.left:
            return self.hasPathSum(root.left, sum-root.val)
        
        if root.right:
            return self.hasPathSum(root.right, sum-root.val)