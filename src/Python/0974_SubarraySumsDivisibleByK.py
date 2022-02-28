class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        sums = 0
        mod_index_dict = {0:1}
        for i, num in enumerate(nums):
            sums += num
            mod = sums % k
            if mod not in mod_index_dict:
                mod_index_dict[mod] = 1
            else:
                count += mod_index_dict[mod]
                mod_index_dict[mod] += 1
        return count