'''

94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        if not root.right and not root.left:
            return [root.val]
        if not root.left:
            return [root.val] + self.inorderTraversal(root.right)
        if not root.right:
            return self.inorderTraversal(root.left) + [root.val]
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)