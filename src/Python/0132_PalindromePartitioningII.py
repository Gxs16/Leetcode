class Solution:
    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def findPalindrome(self, s, start, used, g):
        candidate = []
        for end in range(start, len(s)):
            if g[start][end]:
                if end == len(s) - 1:
                    return True
                if used[end+1] == 0:
                    candidate.append(end+1)
                    used[end+1] = 1
        return candidate

    def cutPalindrome(self, s, used, candidate, g):
        candidate_next = []
        for cand in candidate:
            result = self.findPalindrome(s, cand, used, g)
            if result is True:
                return 0
            else:
                candidate_next.extend(result)
        return self.cutPalindrome(s, used, candidate_next, g)+1

    def minCut(self, s: str) -> int:
        n = len(s)
        g = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]

        used = {}
        for i in range(n):
            used[i] = 0
        used[0] = 1
        candidate = self.findPalindrome(s, 0, used, g)
        if candidate is True:
            return 0
        else:
            return self.cutPalindrome(s, used, candidate, g)+1

class Solution:
    def minCut(self, s: str) -> int:
        dp = [[True]*(len(s)) for i in range(len(s))]
        for i in range(len(s)):
            for j in range(i-1, -1, -1):
                if s[i] == s[j]:
                    dp[j][i] = dp[j+1][i-1]
                else:
                    dp[j][i] = False
        
        stack = []
        traverse = set()
        for i in range(0, len(s)):
            if dp[0][i]:
                stack.append((0, i))
                traverse.add(i)

        while stack:
            count, start = stack.pop(0)
            if start == len(s)-1:
                return count
            else:
                for i in range(len(s)-1, start, -1):
                    if dp[start+1][i] and i not in traverse:
                        stack.append((count+1, i))
                        traverse.add(i)


