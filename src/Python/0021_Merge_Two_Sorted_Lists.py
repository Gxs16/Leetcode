'''
@Author: Xinsheng Guo
@Time: 2020年12月30日16:27:37
@File: 0021_Merge_Two_Sorted_Lists.py
@Link: https://leetcode-cn.com/problems/merge-two-sorted-lists/
@Tag: Linked List; Two Pointers
'''
#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and l2:
            return l2
        elif l1 and not l2:
            return l1
        elif l1 and l2:
            if l2.val >= l1.val:
                result = l1
                result.next = self.mergeTwoLists(l1.next, l2)
            else:
                result = l2
                result.next = self.mergeTwoLists(l2.next, l1)
            return result
# @lc code=end

