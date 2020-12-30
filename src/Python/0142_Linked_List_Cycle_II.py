'''
@Author: Xinsheng Guo
@Time: 2020-11-29 18:13:34
@File: 0142_Linked_List_Cycle_II.py
@Link: https://leetcode-cn.com/problems/linked-list-cycle-ii/
@Tag: Linked List; Two Pointers
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        try:
            fast = head.next.next
            slow = head.next
        except:
            return
        while fast != slow:
            try:
                fast = fast.next.next
                slow = slow.next
            except:
                return
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
