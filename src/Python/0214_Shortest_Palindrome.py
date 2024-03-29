class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        base, mod = 131, 10**9 + 7
        left = right = 0
        mul = 1
        best = -1
        
        for i in range(n):
            left = (left * base + ord(s[i])) % mod
            right = (right + (mul% mod) * ord(s[i])) % mod
            if left == right:
                best = i
            mul = mul * base 
        
        add = ("" if best == n - 1 else s[best+1:])
        return add[::-1] + s
