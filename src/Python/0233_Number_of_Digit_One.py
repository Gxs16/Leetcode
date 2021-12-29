from functools import cache

class Solution:
    @ cache
    def countDigit(self, num, n):
        m = len(num)
        if m == 1:
            if num[0] == 0:
                return 0
            else:
                return 1
        else:
            if num[-1] == 1:
                return self.countDigit((9,)*(m-1), n)+self.countDigit(num[0:m-1], n)+1+n%(10**(m-1))
            elif num[-1] > 1:
                return self.countDigit((9,)*(m-1), n)*num[-1]+10**(m-1)+self.countDigit(num[0:m-1], n)
            else:
                return self.countDigit(num[0:m-1], n)


    def countDigitOne(self, n: int) -> int:
        i = 1
        num = []
        n_temp = n
        if n == 0:
            return 0
        while n > 0:
            num.append((n%(10*i))//i)
            n //= 10
        return self.countDigit(tuple(num), n_temp)