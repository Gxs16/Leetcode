class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        xor = [0]
        for i in arr:
            xor.append(xor[-1]^i)
        n = len(arr)
        result = 0
        for i in range(1, n):
            for j in range(i+1, n+1):
                if xor[j]^xor[i-1] == 0:
                    result += j-i
        return result
