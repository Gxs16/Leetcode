class Solution:
    def max_path(self, node):
        if node.left:
            left_half, left_max = self.max_path(node.left)
        else:
            left_max = float('-inf')
            left_half = 0

        if node.right:
            right_half, right_max = self.max_path(node.right)
        else:
            right_max = float('-inf')
            right_half = 0

        return max(left_half, right_half, 0)+node.val, max(node.val+left_half+right_half, left_max, right_max, node.val, node.val+left_half, node.val+right_half)

    def maxPathSum(self, root) -> int:
        _, path_max = self.max_path(root)

        return path_max
