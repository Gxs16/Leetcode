'''
@Author: Xinsheng Guo
@Time: 2020年12月28日17:36:34
@File: 0206_Reverse_Linked_List.py
@Link: https://leetcode-cn.com/problems/reverse-linked-list/
@Tag: Linked List
'''
#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#%%
class ListNode:
    def __init__(self, x, thenext=None):
        self.val = x
        self.next = thenext
# @lc code=start
# Definition for singly-linked list.
class Solution:
    def reverse(self, head: ListNode, last: ListNode):
        if head:
            _next = last.next
            if _next:
                _n_next = _next.next
                last.next = _n_next
                _next.next = head
                _next = self.reverse(_next, last)
                return _next
            else:
                return head
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(head, head)
# @lc code=end
#%%
a5 = ListNode(5)
a4 = ListNode(4, a5)
a3 = ListNode(3, a4)
a2 = ListNode(2, a3)
a1 = ListNode(1, a2)
Solution().reverseList(a1)
# %%
