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
    def findnext(self, root) -> int:
        while root.left:
            root = root.left
        return root.val
    
    def findprev(self, root) -> int:
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root:
            if root.val == key:
                if not root.left and not root.right:
                    root = None
                elif not root.right and root.left:
                    root.val = self.findprev(root.left)
                    root.left = self.deleteNode(root.left, root.val)
                else:
                    root.val = self.findnext(root.right)
                    root.right = self.deleteNode(root.right, root.val)
            elif root.val > key and root.left:
                root.left = self.deleteNode(root.left, key)
            elif root.val < key and root.right:
                root.right = self.deleteNode(root.right, key)
        return root
        
# @lc code=end

#%%
a1 = TreeNode(35)
b1 = TreeNode(39)
c1 = TreeNode(42)
d1 = TreeNode(44)
e1 = TreeNode(48)

a2 = TreeNode(36, a1, b1)
b2 = TreeNode(43, c1, d1)
c2 = TreeNode(val=46, right=e1)

a3 = TreeNode(val=34, right=a2)
b3 = TreeNode(45, b2, c2)

a4 = TreeNode(val=40, left=a3, right=b3)

a5 = TreeNode(val=33, right=a4)

a6 = TreeNode(val=2, right=a5)

Solution().deleteNode(a6, 33)

# %%
a = TreeNode(1)
b = TreeNode(val=2, left=a)
Solution().deleteNode(b, 2)