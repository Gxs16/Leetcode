'''
@Author: Xinsheng Guo
@Time: 2020-12-12 23:00:30
@File: 0144_Binary_Tree_Preorder_Traversal.py
@Link: https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
@Tag: Graph; Depth-first Search; Breadth-first Search
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        stack = [root]
        result = []
        searched = set()
        while stack:
            x = stack.pop()
            if x is None:
                continue
            if not x in searched:
                stack.extend([x.right, x.left, x])
                searched.add(x)
            else:
                result.append(x.val)
        return result