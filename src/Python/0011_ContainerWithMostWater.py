class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        i = 0
        j = len(height)-1
        while j > i:
            if height[j] > height[i]:
                result = max(result, (j-i)*height[i])
                i += 1
            elif height[j] < height[i]:
                result = max(result, (j-i)*height[j])
                j -= 1
            else:
                result = max(result, (j-i)*height[j])
                j -= 1
                i += 1
        return result