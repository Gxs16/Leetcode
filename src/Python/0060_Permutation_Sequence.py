class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = ''
        factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        number = [i for i in range(1, n+1)]
        for i in factorial[n-1::-1]:
            mod = k//i
            k = k%i
            if k == 0:
                result += str(number.pop(mod-1))
            else:
                result += str(number.pop(mod))
        return result
