class BinaryIndexedTree:
    def __init__(self, length):
        self.c = [0] * length
        self.length = length

    def lowBit(self, x):
        return x & (-x)
    
    def update(self, pos, value=1):
        while pos < self.length:
            self.c[pos] += value
            pos += self.lowBit(pos)
    
    def query(self, pos):
        ans = 0
        while pos > 0:
            ans += self.c[pos]
            pos -= self.lowBit(pos)
        return ans


class Solution:
    def discretization(self, nums):
        a = sorted(set(nums))
        value2ID = {v : i + 1 for i, v in enumerate(a)}
        return value2ID, len(a)

    def countSmaller(self, nums):
        value2ID, length = self.discretization(nums)
        BIT = BinaryIndexedTree(length + 1)
        ans = []

        for i in nums[::-1]:
            posID = value2ID[i]
            ans.append(BIT.query(posID - 1))
            BIT.update(posID)
        
        return ans[::-1]