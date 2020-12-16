'''
@Author: Xinsheng Guo
@Time: 2020-12-16 13:55:42
@File: 0098_Validate_Binary_Search_Tree.py
@Link: https://leetcode-cn.com/problems/validate-binary-search-tree/
@Tag: Tree; Depth-first Search; Recursion
'''
#%%
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 记录当前根节点下所有节点的最大值和最小值
        max_value_dict = dict()
        min_value_dict = dict()
        def validate(root, max_value_dict, min_value_dict):
            if (root.left is None) and (root.right is None):
                max_value_dict[root] = root.val
                min_value_dict[root] = root.val
                return True
            elif (root.left is None) and root.right:
                result = validate(root.right, max_value_dict, min_value_dict)
                if result:
                    if root.val < min_value_dict[root.right]:
                        min_value_dict[root] = root.val
                        max_value_dict[root] = max_value_dict[root.right]
                        return True
            elif root.left and (root.right is None):
                result = validate(root.left, max_value_dict, min_value_dict)
                if result:
                    if root.val > max_value_dict[root.left]:
                        max_value_dict[root] = root.val
                        min_value_dict[root] = max_value_dict[root.left]
                        return True
            else:
                result = validate(root.left, max_value_dict, min_value_dict) \
                         and validate(root.right, max_value_dict, min_value_dict)
                if result:
                    if root.val > max_value_dict[root.left]\
                        and root.val < min_value_dict[root.right]:
                        min_value_dict[root] = min_value_dict[root.left]
                        max_value_dict[root] = max_value_dict[root.right]
                        return True
            return False
        if root:
            return validate(root, max_value_dict, min_value_dict)
        else:
            return False

#%%
a = TreeNode(3)
b = TreeNode(7)
c = TreeNode(6, a, b)
d = TreeNode(4)
e = TreeNode(5, d, c)
Solution().isValidBST(e)
# %%
