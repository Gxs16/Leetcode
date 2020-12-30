'''
@Author: Xinsheng Guo
@Time: 2020-12-1 23:03:05
@File: 0209_Minimum_Size_Subarray_Sum.py
@Link: https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
@Tag: Linked List; Two Pointers
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        forward = head
        psuehead = ListNode(next=head)
        backward = psuehead
        for i in range(n):
            forward = forward.next
        while forward:
            forward = forward.next
            backward = backward.next

        backward.next = backward.next.next
        return psuehead.next
