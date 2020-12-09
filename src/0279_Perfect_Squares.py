'''
@Author: Xinsheng Guo
@Time: 2020-12-6 23:40:56
@File: 0279_Perfect_Squares.py
@Link: https://leetcode-cn.com/problems/perfect-squares/
@Tag: Array
'''
#%%
import math
class Solution:
    def numSquares(self, n: int) -> int:
        x = int(math.sqrt(n))
        if x**2 != n:
            a = n
            for i in range(int(x/math.sqrt(2))):
                target = n - (x-i)**2
                num = 1 + self.numSquares(target)
                if num <= a:
                    a = num
            return a
        else:
            return 1
#%%
import math
int(math.sqrt(5))**2
# %%
Solution().numSquares(2)
# %%
class Solution:
    def construct_queue(self, queue: set, count: int) -> int:
        queue = list(queue)
        queue_new = set()
        while queue:
            n = queue.pop(0)
            x = int(n**0.5)
            if (x)**2 == n:
                break
            else:
                for i in range(x):
                    target = n - (x-i)**2
                    queue_new.add(target)
        else:
            count = self.construct_queue(queue_new, count)
        return count+1

    def numSquares(self, n: int) -> int:
        return self.construct_queue({n}, 0)
# %%
