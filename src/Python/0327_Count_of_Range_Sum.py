from functools import cache
class BinaryIndexedTree:
    def __init__(self, length):
        self.c = [0] * length
        self.length = length

    def lowBit(self, x):
        return x & (-x)
    
    def update(self, pos, value=1):
        while pos < self.length:
            self.c[pos] += value
            pos += self.lowBit(pos)
    @cache
    def query(self, pos):
        ans = 0
        while pos > 0:
            ans += self.c[pos]
            pos -= self.lowBit(pos)
        return ans

class Solution:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        length = len(nums)
        BIT = BinaryIndexedTree(length+1)
        result = 0
        for i in range(length):
            BIT.update(i+1, nums[i])
            if nums[i]<=upper and nums[i]>=lower:
                result += 1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sums = BIT.query(j+1)-BIT.query(i)
                if sums>=lower and sums<=upper:
                    result += 1
        return result

class Solution:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        presum = []
        sums = 0
        for i in nums:
            sums += i
            presum.append(sums)

        presum.sort()
        left = 0
        right = 0
        result = 0
        for i in presum:
            while left<len(presum) and presum[left]-i < lower:
                left += 1
            while right<len(presum) and presum[right]-i <= right:
                right += 1
            result += right - left
        return result