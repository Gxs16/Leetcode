class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0:1}
        result = 0
        sums = 0
        for i in nums:
            sums += i
            if sums-k in count:
                result += count[sums-k]
            if sums in count:
                count[sums] += 1
            else:
                count[sums] = 1
        return result