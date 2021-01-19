'''
@Author: Xinsheng Guo
@Time: 2021年1月19日14:05:54
@File: 0328_Odd_Even_Linked_List.py
@Link: https://leetcode-cn.com/problems/odd-even-linked-list/
@Tag: Linked List
'''
#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head
        left = head
        mid = left.next
        right = head.next.next
        while right.next and right.next.next:
            temp1 = left.next
            temp2 = right
            temp3 = mid
            mid = right.next
            right = right.next.next
            temp3.next = temp2.next
            left.next = temp2
            temp2.next = temp1
            left = temp2
        temp1 = left.next
        mid.next = right.next
        left.next = right
        right.next = temp1
        return head
# @lc code=end

