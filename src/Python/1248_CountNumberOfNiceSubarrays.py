class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        sums = 0
        count = {0:1}
        result = 0
        for i in nums:
            if i % 2 == 0:
                pass
            else:
                sums += 1
            if sums in count:
                count[sums] += 1
            else:
                count[sums] = 1
            if sums-k in count:
                result += count[sums-k]
        return result