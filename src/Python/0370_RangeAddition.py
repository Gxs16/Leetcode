class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        result = [0] * (length+1)
        for start, end, inc in updates:
            result[start] += inc
            result[end+1] -= inc

        for i in range(1, length):
            result[i] += result[i-1]

        return result[:-1]

#%%
(2 ^ 3)^2
# %%
6^8