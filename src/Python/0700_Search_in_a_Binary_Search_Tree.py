'''
@Author: Xinsheng Guo
@Time: 2020-12-17 11:18:50
@File: 0700_Search_in_a_Binary_Search_Tree.py
@Link: https://leetcode-cn.com/problems/search-in-a-binary-search-tree/
@Tag: 
'''
#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @lc code=start
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            if root.val == val:
                return root
            elif root.val > val and root.left:
                return self.searchBST(root.left, val)
            elif root.val < val and root.right:
                return self.searchBST(root.right, val)
        else:
            return None
# @lc code=end
