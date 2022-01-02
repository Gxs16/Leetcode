# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root:
            stack = [root]
            result = [root.val]

            for i in stack:
                if i.left:
                    stack.append(i.left)
                    result.append(i.left.val)
                else:
                    result.append(None)

                if i.right:
                    stack.append(i.right)
                    result.append(i.right.val)
                else:
                    result.append(None)
            while result[-1] is None:
                result.pop()
            return str(result)
        else:
            return ''

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if data:
            data = data[1:-1]
            data = data.split(', ')
            root = TreeNode(val=int(data.pop(0)))
            stack = [root]
            for node in stack:
                if data:
                    value = data.pop(0)
                    if value != 'None':
                        leftnode = TreeNode(val=int(value))
                        node.left = leftnode
                        stack.append(leftnode)
                if data:
                    value = data.pop(0)
                    if value != 'None':
                        rightnode = TreeNode(val=int(value))
                        node.right = rightnode
                        stack.append(rightnode)
            return root
        else:
            return None