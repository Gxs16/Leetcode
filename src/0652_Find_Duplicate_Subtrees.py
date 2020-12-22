'''
@Author: Xinsheng Guo
@Time: 2020年12月22日15:27:49
@File: 0652_Find_Duplicate_Subtrees.py
@Link: https://leetcode-cn.com/problems/find-duplicate-subtrees/
@Tag: Tree
'''
#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#
#%%
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
from collections import defaultdict
class Solution:
    def inorder_traversal(self, root, sub_dict):
        if root:
            result = []
            result.append(root.val)
            result.extend(self.inorder_traversal(root.left, sub_dict))
            result.extend(self.inorder_traversal(root.right, sub_dict))
            sub_dict[tuple(result)].append(root)
        else:
            result = [None]
        return result
    def findDuplicateSubtrees(self, root: TreeNode):
        sub_dict = defaultdict(list)
        self.inorder_traversal(root, sub_dict)
        result = [i[0] for i in sub_dict.values() if len(i) > 1]
        return result
# @lc code=end
#%%
a = TreeNode(val=0)
b1 = TreeNode(val=0)
b2 = TreeNode(val=0, right=a)
c1 = TreeNode(val=0, left=b1)
c2 = TreeNode(val=0, right=b2)
d = TreeNode(val=0, left=c1, right=c2)
Solution().findDuplicateSubtrees(d)
#%%
'a'+'b'
# %%
str(None)
# %%
