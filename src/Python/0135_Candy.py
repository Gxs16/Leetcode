'''
@Author: Xinsheng Guo
@Time: 2021年12月1日
@File: 0135_Candy.py
@Link: https://leetcode-cn.com/problems/candy/
'''
#%%
class Solution:
    def candy(self, ratings: list) -> int:
        total = 0
        ratings = [ratings[0]]+ratings+[ratings[-1]]
        min_index = 0
        for middle in range(1, len(ratings)-1):
            left = middle-1
            right = middle+1
            if ratings[left] == ratings[middle] and ratings[middle] < ratings[right]:
                min_index = middle
            elif ratings[left] == ratings[middle] and ratings[right] == ratings[middle]:
                if min_index == middle-1:
                    total += 1
                else:
                    dis_left = max_index-min_index
                    dis_right = middle-max_index
                    min_dis = min(dis_left, dis_right)
                    max_dis = max(dis_left, dis_right)
                    total += (2+max_dis)*(1+max_dis)/2
                    total += (1+min_dis)*min_dis/2
                min_index = middle 
            elif ratings[left] > ratings[middle] and ratings[right] >= ratings[middle]:
                dis_left = max_index-min_index
                dis_right = middle-max_index
                min_dis = min(dis_left, dis_right)
                max_dis = max(dis_left, dis_right)
                total += (2+max_dis)*(1+max_dis)/2
                total += (1+min_dis)*min_dis/2
                min_index = middle
            elif ratings[left] < ratings[middle] and ratings[middle] == ratings[right]:
                max_index = middle
            elif ratings[left] == ratings[middle] and ratings[middle] > ratings[right]:
                max_index = middle
            elif ratings[left] < ratings[middle] and ratings[middle] > ratings[right]:
                max_index = middle
        return int(total)
            
# %%
Solution().candy([1,0,2])
# %%
a = [1,2,3,4,5,4,2,1]
a.pop(0)
a