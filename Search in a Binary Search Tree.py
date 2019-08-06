'''

LeetCode 700. Search in a Binary Search Tree
https://leetcode.com/problems/search-in-a-binary-search-tree/

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root and val<root.val: 
            return self.searchBST(root.left, val)
        elif root and val>root.val:
            return self.searchBST(root.right, val)
        
        return root