class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sums = 0
        mod_index_dict = {0:-1}
        for i, num in enumerate(nums):
            sums += num
            mod = sums % k
            if mod not in mod_index_dict:
                mod_index_dict[mod] = i
            elif mod_index_dict[mod] < i-1:
                return True
        return False
