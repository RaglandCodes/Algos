'''

Leetcode 1022. Sum of Root To Leaf Binary Numbers
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/submissions/

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        a = []

        def s(root, a):
            l = None
            r = None
            if root.left:
                if a == []:
                    a = [str(root.val)]
                else:
                    for i in range(len(a)):
                        a[i] = str(root.val) + a[i]
                l =  s(root.left, a)

            if root.right:
                if a == []:
                    a = [str(root.val)]
                else:
                    for i in range(len(a)):
                        a[i] = str(root.val) + a[i]
                r = s(root.right, a)
            
            if l is None and r is None:
                return [str(root.val)]
            

            if l is None:
                l = r
            elif r is None:
                pass        # l = l
            else:
                l += r
        
            for i in range(len(l)):
                l[i] = str(root.val) + l[i]
                    
            return l
        
        b = s(root, a)
        
        for i in range(len(b)):
            b[i] = int(b[i], 2)
            
        return sum(b)
            
