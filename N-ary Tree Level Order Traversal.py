'''

Leetcode 429. N-ary Tree Level Order Traversal
https://leetcode.com/problems/n-ary-tree-level-order-traversal/

'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        a = []
        q = [[root, 0]]
        
        while q:
            
            if q[0][1] >= len(a):
                a += [[q[0][0].val]]
            else:
                a[q[0][1]] += [q[0][0].val]
            
            c = q[0][0].children
            
            for i in range(len(c)):
                c[i] = [c[i], q[0][1] + 1]
            
            q += c
            q.pop(0)
        
        return a
            