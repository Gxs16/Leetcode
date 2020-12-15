'''
@Author: Xinsheng Guo
@Time: 2020-12-15 19:52:19
@File: 0101_Symmetric_Tree.py
@Link: https://leetcode-cn.com/problems/symmetric-tree/
@Tag: Tree; Depth-first Search; Breadth-first Search
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            queue = [[root]]
        else:
            return False
        while queue:
            _result = []
            _leaves = []
            leaves = queue.pop(0)
            for i in leaves:
                if i:
                    if i.left:
                        _leaves.append(i.left)
                        _result.append(i.left.val)
                    else:
                        _result.append(i.left)
                    if i.right:
                        _leaves.append(i.right)
                        _result.append(i.right.val)
                    else:
                        _result.append(i.right)
            if _leaves:
                queue.append(_leaves)
            if _result[::-1] != _result:
                return False
        return True
#%%
a = [1,2,1]
a[::-1] == a
# %%
