'''

LeetCode 234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        first_half = []
        
        p1 = head
        p2 = head
        
        while p2 != None:
            first_half += [p1.val]
            p1 = p1.next
            if p2.next is None:
                p2 = p2.next
                first_half.pop()
            else:
                p2 = p2.next.next
            
        first_half = first_half[::-1]
        
        for n in first_half:
            if n != p1.val:
                return False
            
            p1 = p1.next
            
        return True
                