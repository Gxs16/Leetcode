'''
@Author: Xinsheng Guo
@Time: 2020-10-21 16:52
@File: 0002_Add_Two_Numbers.py
@Link: https://leetcode-cn.com/problems/add-two-numbers/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is not None and l2 is not None:
            l1.val += l2.val
            if l1.val >= 10:
                l1.val -= 10
                if l1.next is not None:
                    l1.next.val += 1
                else:
                    l1.next = ListNode(1)
            l1.next = self.addTwoNumbers(l1.next, l2.next)
            return l1
        elif l1 is None and l2 is not None:
            return l2
        elif l1 is not None and l2 is None:
            if l1.val >= 10:
                l1.val -= 10
                if l1.next is not None:
                    l1.next.val += 1
                    if l1.next.val >= 10:
                        l1.next = self.addTwoNumbers(l1.next, l2=None)
                else:
                    l1.next = ListNode(1)
            return l1
        else:
            return None
        
if __name__=='__main__':
    pass
