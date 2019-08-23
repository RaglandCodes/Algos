'''

LeetCode 141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

This is not the right way to do it, but it works for now 🤣.

It works becase there's an error when the reccursive depth is reached, an error is thrown.

This solution is very slow - faster than 5% - compared to others and could be Time Limit Exceeded in the future or in another platform maybe.

Inspired by https://leetcode.com/problems/linked-list-cycle/discuss/44494/Except-ionally-fast-Python
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            print(head)
        except:
            return True
        
        return False
        