class Solution:
    def largestRectangleArea(self, heights) -> int:
        stack = [(-1, -1)]
        result_left = [-1 for i in heights]
        result_right = [len(heights) for i in heights]
        for index, value in enumerate(heights):
            while stack[-1][1] >= value:
                result_right[stack[-1][0]] = index
                stack.pop()
            else:
                result_left[index] = stack[-1][0]
                stack.append((index, value))
        result_max = max(value*(result_right[index]-result_left[index]-1) for index, value in enumerate(heights))
        return result_max
