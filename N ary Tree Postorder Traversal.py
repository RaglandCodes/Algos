'''

LeetCode 590. N-ary Tree Postorder Traversal
https://leetcode.com/problems/n-ary-tree-postorder-traversal/

Answer from https://leetcode.com/problems/n-ary-tree-postorder-traversal/discuss/155806/Python-iterative-and-recursive-solution-with-explanation

'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        result = []
        
        if root is None:
            return result
        
        def postorder_resursion(root, result):
            for child in root.children:
                postorder_resursion(child, result)
            
            result.append(root.val)
             
        postorder_resursion(root, result) 
        return result