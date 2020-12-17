'''
@Author: Xinsheng Guo
@Time: 2020-12-17 16:42:07
@File: 0450_Delete_Node_in_BST.py
@Link: https://leetcode-cn.com/problems/delete-node-in-a-bst/
@Tag: Array
'''
#%%
#
# @lc app=leetcode.cn id=450 lang=python3#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start

class Solution:
    def findNode(self, root, val, father_dict):
        if root:
            if root.val == val:
                return root
            elif root.val > val and root.left:
                father_dict[root.left] = (root, 'left')
                return self.findNode(root.left, val, father_dict)
            elif root.val < val and root.right:
                father_dict[root.right] = (root, 'right')
                return self.findNode(root.right, val, father_dict)
        else:
            return root
    
    def findnext(self, root):
        if root.left:
            return self.findnext(root.left)
        else:
            return root

    def deleteNode(self, root: TreeNode, key: int):
        father_dict = dict()
        target = self.findNode(root, key, father_dict)
        if target:
            if not target.left and not target.right:
                if target is root:
                    return None
                setattr(father_dict[target][0], father_dict[target][1], None)
            elif not target.left and target.right:
                alpha = target.right.val
                self.deleteNode(target, alpha)
                target.val = alpha
            elif target.left and not target.right:
                alpha = target.left.val
                self.deleteNode(target, alpha)
                target.val = alpha
            else:
                target_next = self.findnext(target.right)
                alpha = target_next.val
                self.deleteNode(target, alpha)
                target.val = alpha
        return root
        
# @lc code=end

#%%
a = TreeNode(2)
b = TreeNode(4)
c = TreeNode(7)
d = TreeNode(3, a, b)
e = TreeNode(6, None, c)
f = TreeNode(5, d, e)
Solution().deleteNode(f, 6)

# %%
