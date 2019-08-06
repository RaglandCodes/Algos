'''
LeetCode 938. Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/submissions/

Got solution from https://leetcode.com/problems/range-sum-of-bst/discuss/288093/Python-commented-solution
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        total = 0
        
        def find_total(root, L, R):
            if root.left:
                find_total(root.left, L, R)
            
            if root.val >= L and root.val <= R:
                nonlocal total
                total += root.val
            
            if root.right:
                find_total(root.right, L, R)
            
        
        find_total(root, L, R)
        
        return total