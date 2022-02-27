class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        result = 0
        index_dict = {0: -1}
        sums = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                sums += 1
            else:
                sums -= 1
            if sums not in index_dict:
                index_dict[sums] = i
            if sums in index_dict:
                result = max(result, i-index_dict[sums])
        return result
