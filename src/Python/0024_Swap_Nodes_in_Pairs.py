'''
@Author: Xinsheng Guo
@Time: 2020-12-10 14:54:26
@File: 0024_Swap_Nodes_in_Pairs.py
@Link: https://leetcode-cn.com/problems/swap-nodes-in-pairs/
@Tag: Linked List
'''
#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
#%%
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            next_node = head.next
            next_next_node = next_node.next
            head.next = self.swapPairs(next_next_node)
            next_node.next = head
            return next_node
        else:
            return head
# @lc code=end
#%%
a4 = ListNode(4)
a3 = ListNode(3, a4)
a2 = ListNode(2, a3)
a1 = ListNode(1, a2)
Solution().swapPairs(a1)