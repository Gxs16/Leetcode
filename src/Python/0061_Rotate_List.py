'''
@Author: Xinsheng Guo
@Time: 2021年1月21日15:09:20
@File: 0061_Rotate_List.py
@Link: https://leetcode-cn.com/problems/rotate-list/
@Tag: Linked List; Two Pointers
'''
#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        fast = head
        length = 1
        while fast.next:
            length += 1
            fast = fast.next
        k = k%length
        slow = head
        for i in range(length-1-k):
            slow = slow.next
        fast.next = head
        head = slow.next
        slow.next = None
        return head
# @lc code=end

