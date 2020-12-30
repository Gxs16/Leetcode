'''
@Author: Xinsheng Guo
@Time: 2020-12-12 23:00:40
@File: 0145_Binary_Tree_Postorder_Traversal.py
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
    def postorderTraversal(self, root: TreeNode):
        stack = [root]
        result = []
        searched = set()
        while stack:
            x = stack.pop()
            if x is None:
                continue
            if not x in searched:
                stack.extend([x.left, x, x.right])
                searched.add(x)
            else:
                result.append(x.val)
        return result