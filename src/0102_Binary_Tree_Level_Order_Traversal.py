'''
@Author: Xinsheng Guo
@Time: 2020-12-15 10:02:52
@File: 0102_Binary_Tree_Level_Order_Traversal.py
@Link: https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
@Tag: Tree; Breadth-first Search
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        result = []
        if root:
            queue = [[root]]
        else:
            return result
        while queue:
            _result = []
            _leaves = []
            leaves = queue.pop(0)
            for i in leaves:
                _result.append(i.val)
                if i.left:
                    _leaves.append(i.left)
                if i.right:
                    _leaves.append(i.right)
            if _leaves:
                queue.append(_leaves)
            result.append(_result)
        return result
            