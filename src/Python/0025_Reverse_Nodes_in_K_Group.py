'''
@Author: Xinsheng Guo
@Time: 2021年12月4日
@File: 0025_Reverse_Nodes_in_K_Group.py
@Link: https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        left = head
        right = left
        while right:
            for i in range(k-1):
                temp = right.next
                right.next = temp.next
                temp.next = left
                left = temp
            head = left
            left = right.next
            right = left

        return head