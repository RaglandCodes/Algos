'''

LeetCode 1290. Convert Binary Number in a Linked List to Integer

https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/submissions/

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        a = ''
        ch = head           # ch -> current head
        while ch != None:
            a += str(ch.val)
            ch = ch.next
            
        return (int(a, 2))