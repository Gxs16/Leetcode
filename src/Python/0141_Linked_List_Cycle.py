'''
@Author: Xinsheng Guo
@Time: 2020-11-29 18:13:34
@File: 0141_Linked_List_Cycle.py
@Link: https://leetcode-cn.com/problems/linked-list-cycle/
@Tag: Linked List; Two Pointers
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        try:
            fast = head.next.next
            slow = head.next
        except:
            return False
        while fast != slow:
            try:
                fast = fast.next.next
                slow = slow.next
            except:
                return False
        return True
        