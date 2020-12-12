'''
@Author: Xinsheng Guo
@Time: 2020-12-12-23:00:50
@File: 0102_Binary_Level_Order_Traversal.py
@Link: https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
@Tag: Graph; Depth-first Search; Breadth-first Search
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode):
        stack = [root]
        result = []
        searched = set()
        while stack:
            x = stack.pop(0)
            if x is None:
                continue
            if not x in searched:
                stack.extend([x.left, x.right])
                searched.add(x)
            else:
                result.append(x.val)
        return result