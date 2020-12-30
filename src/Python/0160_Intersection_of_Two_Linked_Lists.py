'''
@Author: Xinsheng Guo
@Time: 2020-11-30 23:16:52
@File: 0160_Intersection_of_Two_Linked_Lists.py
@Link: https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
@Tag: Two Pointers; Linked List
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB
        while pA != pB:
            if pA:
                pA = pA.next
                if pB:
                    pB = pB.next
                else:
                    pB = headA
            else:
                pA = headB
                if pB:
                    pB = pB.next
                else:
                    return
        return pA