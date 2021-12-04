'''
@Author: Xinsheng Guo
@Time: 2021年12月3日
@File: 0021_Merge_k_Sorted_Lists.py
@Link: https://leetcode-cn.com/problems/merge-k-sorted-lists/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

    def mergeKLists(self, lists: List[ListNode]):
        if lists:
            while len(lists) > 1:
                result = []
                if len(lists)%2 == 1:
                    lists.append(lists.pop())
                for i in range(0, len(lists), 2):
                    result.append(self.mergeTwoLists(lists[i], lists[i+1]))
                lists = result
            return lists[0]
