'''

LeetCode 83. Remove Duplicates from Sorted List

Solution from https://leetcode.com/problems/remove-duplicates-from-sorted-list/discuss/333278/Best-Python-Solution-(Set-Pointers-Explained)

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head is None or head.next is None:
            return head
        
        prev = head
        items = [prev.val]
        cur = head.next
        
        while cur:
            if cur.val in items:
                prev.next = cur.next
            else:
                items += [cur.val]
                prev = prev.next
                
            
            cur = cur.next
            
        return head
        
        
    