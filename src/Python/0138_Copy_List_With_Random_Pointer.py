'''
@Author: Xinsheng Guo
@Time: 2021年1月20日11:33:39
@File: 0138_Copy_List_With_Random_Pointer.py
@Link: https://leetcode-cn.com/problems/copy-list-with-random-pointer/
@Tag: Hash Table; Bit Manipulation
'''
#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#



# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# @lc code=start
class Solution:
    def copyRandomList(self, head):
        copy_dict = {None: None}
        target = head
        while target:
            if not target.next in copy_dict:
                copy_dict[target.next] = Node(x=target.next.val)
            if not target.random in copy_dict:
                copy_dict[target.random] = Node(x=target.random.val)

            if not target in copy_dict:
                copy_dict[target] = Node(x=target.val, next=copy_dict[target.next], random=copy_dict[target.random])
            else:
                copy_dict[target].next = copy_dict[target.next]
                copy_dict[target].random = copy_dict[target.random]
            target = target.next

        return copy_dict[head]   
# @lc code=end
