'''
@Author: Xinsheng Guo
@Time: 2020-12-17 11:18:50
@File: 0701_Insert_into_a_Binary_Search_Tree.py
@Link: https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/
@Tag: Tree
'''
#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root.val > val and root.left:
            return self.searchBST(root.left, val)
        elif root.val < val and root.right:
            return self.searchBST(root.right, val)
        else:
            return root

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            position = self.searchBST(root, val)
            if position.val > val:
                position.left = TreeNode(val=val)
            else:
                position.right = TreeNode(val=val)
        else:
            root = TreeNode(val=val)
        return root
# @lc code=end

