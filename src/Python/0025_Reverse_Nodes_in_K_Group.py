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
        if k == 1 or (not head.next):
            return head
        left = ListNode(val=0, next=head)
        start = left
        right = head
        is_break = False
        while right:
            detect = right
            for j in range(k-1):
                if detect.next:
                    detect = detect.next
                else:
                    is_break = True
                    break
            if is_break:
                break
            for i in range(k-1):
                temp = right.next
                right.next = temp.next
                temp.next = left.next
                left.next = temp
            left = right
            right = right.next
        return start.next