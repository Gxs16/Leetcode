from collections import Counter
from functools import cache
class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        else:
            if Counter(s1) == Counter(s2):
                for i in range(1, len(s1)):
                    if (self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i:], s2[i:])):
                        return True
                    if (self.isScramble(s1[0:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                        return True
        return False