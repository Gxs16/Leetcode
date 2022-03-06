class Solution:
    def xorQueries(self, arr, queries):
        xor = [0]
        for i in arr:
            xor.append(xor[-1]^i)
        result = []
        for start, end in queries:
            result.append(xor[end+1]^xor[start])
        return result
