'''

LeetCode 82. Remove Duplicates from Sorted List II
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head == None:
            return None
        
        p1 = head
        p2 = head
        
        def next_not_n(node):
            val_to_del = node.val
            while node != None:
                if node.val != val_to_del:
                    break
                node = node.next
            
            return node
            
        while p1.next != None:
            if p1.val == p1.next.val:
                if p1 == head:
                    head = next_not_n(p1)
                    p1 = head
                    p2 = head
                else:
                    p2.next = next_not_n(p1)
                    p1 = p2.next
            else:
                p2 = p1
                p1 = p1.next
            
            if p1 == None:
                break
        
        return head
            