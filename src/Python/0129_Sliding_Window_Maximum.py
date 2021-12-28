import collections
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        result = []
        queue = collections.deque()
        for i in range(k):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)

        result.append(nums[queue[0]])

        for i in range(k, len(nums)):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            while queue and queue[0] < i-k:
                queue.popleft()
            result.append(nums[queue[0]])

        return result
        