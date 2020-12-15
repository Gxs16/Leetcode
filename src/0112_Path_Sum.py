'''
@Author: Xinsheng Guo
@Time: 2020-12-15 20:10:45
@File: 0101_Symmetric_Tree.py
@Link: https://leetcode-cn.com/problems/path-sum/
@Tag: Tree; Depth-first Search
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool: