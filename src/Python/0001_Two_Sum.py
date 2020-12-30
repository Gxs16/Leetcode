'''
@Author: Xinsheng Guo
@Time: 2020-10-19 09:58
@File: 0001_Two_Sum.py
@Link: https://leetcode-cn.com/problems/two-sum/
'''

from collections import defaultdict

nums = [1, 8, 7, 12, 2, 3, 4, 6, 5, 9, 10, 0]
target = 10

nums_sup = defaultdict(list)
for i in range(len(nums)):
    nums_sup[target - nums[i]].append(i)

result = []
for i in range(len(nums)):
    try:
        if i < nums_sup[nums[i]][-1]:
            index = nums_sup[nums[i]].pop()
            result.append([i, index])
    except:
        pass

print(result)
