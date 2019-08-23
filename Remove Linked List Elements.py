'''

LeetCode 203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        prev = ptr = head
        
        while ptr != None:
            if ptr.val == val:
                if ptr == head:
                    head = head.next
                    continue
                prev.next = ptr.next
            else:
                prev = ptr

            ptr = ptr.next
            
        return head
        