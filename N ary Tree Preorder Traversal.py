'''

LeetCode 589. N-ary Tree Preorder Traversal

https://leetcode.com/problems/n-ary-tree-preorder-traversal/

Solution from https://leetcode.com/problems/n-ary-tree-preorder-traversal/discuss/283686/Python-easy-recursive-solution-with-commentary

More about extend
 - https://stackoverflow.com/a/24261311/10617695
 - https://stackoverflow.com/questions/252703/what-is-the-difference-between-pythons-list-methods-append-and-extend

'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        result = [root.val]
        
        for child in root.children:
            result.extend(self.preorder(child))
            
        return result
            
        