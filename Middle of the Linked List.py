'''

LeetCode 876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/


One can also use the runner technique. 
The second pointer is travelling twice as fast and we just print the value of the node where the slow pointer is when the fast pointer reaches the end
https://leetcode.com/problems/middle-of-the-linked-list/discuss/154763/Remember-this-pattern-for-problems-that-require-middle-finding-in-a-Linked-List.
https://leetcode.com/problems/middle-of-the-linked-list/discuss/154696/Python-two-pointer-extremely-simple-with-explaination
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 0
        cur = head
        while cur != None:
            length += 1
            cur = cur.next
        cur = head
        
        to_print = length // 2
        i = 0
        while True:
            if i == to_print:
                return cur
            cur = cur.next
            i += 1
        
    