'''

Leetcode 637. Average of Levels in Binary Tree
https://leetcode.com/problems/average-of-levels-in-binary-tree/

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        n = []  #Counts number of nodes in each level
        v = []  #Stores value of sum of nodes in each level
        q = [[root, 0]]
        
        while q:
            
            if not (len(n) > q[0][1]):
                n += [1]
                v += [q[0][0].val]
                
            else:
                n[q[0][1]] += 1
                v[q[0][1]] += q[0][0].val
                
                
            if q[0][0].left:
                q += [[q[0][0].left, q[0][1] + 1]]
                
            if q[0][0].right:
                q += [[q[0][0].right, q[0][1] + 1]]
            
            q.pop(0)
        
        for i, value in enumerate(v):
            v[i] /= n[i]
            
        return v
            