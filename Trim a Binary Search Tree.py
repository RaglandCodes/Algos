'''

Leetcode 669. Trim a Binary Search Tree
https://leetcode.com/problems/trim-a-binary-search-tree/submissions/

Answer from https://www.youtube.com/watch?v=hFwakLj7wFA

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

  #   9
  #  / \
  # 6   11

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        
        if not root:
            return None
        if root.val > R:
            return self.trimBST(root.left, L, R)
        if root.val < L:
            return self.trimBST(root.right, L, R)
        
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        
        return root