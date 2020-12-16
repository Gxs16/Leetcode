'''
@Author: Xinsheng Guo
@Time: 2020-12-15 11:28:53
@File: 0104_Maximum_Depth_of_Binary_Tree.py
@Link: https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
@Tag: Tree; Depth-first Search; Recursion
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        result = 0
        if root:
            queue = [[root]]
        else:
            return result
        while queue:
            _result = []
            _leaves = []
            leaves = queue.pop(0)
            for i in leaves:
                if i.left:
                    _leaves.append(i.left)
                if i.right:
                    _leaves.append(i.right)
            if _leaves:
                queue.append(_leaves)
            result+=1
        return result