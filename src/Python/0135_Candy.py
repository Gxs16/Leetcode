'''
@Author: Xinsheng Guo
@Time: 2021年12月1日
@File: 0135_Candy.py
@Link: https://leetcode-cn.com/problems/candy/
'''
#%%
class Solution:
    def candy(self, ratings: list) -> int:
        reward = [1]
        count = 0
        for i in range(1, len(ratings)):
            if ratings[i] == ratings[i-1]:
                if count > 0:
                    if reward[-1] <= count:
                        reward[-1] = count+1
                    while count > 0:
                        reward.append(count)
                        count -= 1
                reward.append(1)
            elif ratings[i] < ratings[i-1]:
                count += 1
            else:
                if count > 0:
                    if reward[-1] <= count:
                        reward[-1] = count+1
                    while count > 0:
                        reward.append(count)
                        count -= 1
                reward.append(reward[-1]+1)
        if count > 0:
            if reward[-1] <= count:
                reward[-1] = count+1
            while count > 0:
                reward.append(count)
                count -= 1
        return sum(reward)
            
# %%
Solution().candy([1,2,87,87,87,2,1])
# %%
Solution().candy([29,51,87,87,72,12])
# %%
Solution().candy([1,2,3,5,4,3,2,1,4,3,2,1,3,2,1,1,2,3,4])
# %%
