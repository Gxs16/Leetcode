class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sums = [0]
        index_dict = {0: -1}
        result = 0
        for i in range(len(nums)):
            sums.append(sums[-1]+nums[i])
            if sums[-1] not in index_dict:
                index_dict[sums[-1]] = i
            if sums[-1]-k in index_dict:
                result = max(result, i-index_dict[sums[-1]-k])
        return result