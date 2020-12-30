'''
@Author: Xinsheng Guo
@Time: 2020-11-05 22:30
@File: 0007_Reverse_integer.py
@Link: https://leetcode-cn.com/problems/reverse-integer/
'''

class Solution:
    def reverse(self, x: int) -> int:
        a = 0
        i = 1
        num = []
        result = 0
        if x>=0:
            op = 1
        else:
            op = -1
        while a != (x):
            a = x % (op*10**i)
            b = a //(op*10**(i-1))
            num.append(b)
            i+=1
        for i, j in enumerate(num):
            result+=op*j*10**(len(num)-i-1)
        if result > 2**31-1 or result < -2**31:
            return 0
        return result
#%%
def reverse(x: int) -> int:
    rev = 0
    if x>=0:
            op = 1
    else:
            op = -1
    x = op*x
    while x!=0:
        pop = x%(10)
        x = x//(10)
        rev = rev*10 + pop
    rev = rev*op
    if rev > 2**31-1 or rev < -2**31:
        return 0
    return rev

reverse(-123)