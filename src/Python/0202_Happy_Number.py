'''
@Author: Xinsheng Guo
@Time: 2020-12-18 17:33:51
@File: 0202_Happy_Number.py
@Link: https://leetcode-cn.com/problems/happy-number/
@Tag: Hash Table
'''
#%%
class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1
#%%
Solution().isHappy(19)
        
# %%
