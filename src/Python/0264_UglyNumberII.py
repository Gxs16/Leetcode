class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        seen = {1}
        for i in range(n):
            result = heapq.heappop(nums)
            for j in [2, 3, 5]:
                if result * j not in seen:
                    seen.add(result*j)
                    heapq.heappush(nums, result*j)
        return result
