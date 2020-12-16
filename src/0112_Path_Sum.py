'''
@Author: Xinsheng Guo
@Time: 2020-12-15 20:10:45
@File: 0112_Path_Sum.py
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
        if root:
            stack = [root]
            sum_dict = dict()
            sum_dict[root] = root.val
        else:
            return False
        while stack:
            x = stack.pop()
            if (x.left is None) and (x.right is None) and (sum_dict[x] == sum):
                return True
            else:
                if x.right:
                    stack.append(x.right)
                    sum_dict[x.right] = sum_dict[x] + x.right.val
                if x.left:
                    stack.append(x.left)
                    sum_dict[x.left] = sum_dict[x] + x.left.val
        return False