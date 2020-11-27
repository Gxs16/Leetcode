'''
@Author: Xinsheng Guo
@Time: 2020-11-19 23:28:26
@File: 0151_Reverse_Words_in_a_String.py
@Link: https://leetcode-cn.com/problems/longest-common-prefix/
@Tag: String
'''
class Solution:
    def pop_words(self, s, result):
        if not s:
            pass
        else:
            index = len(s)-1
            while s[index] != ' ' and index >= 0:
                index -= 1
            result += s[index+1:]
            result += ' '
            while s[index]==' ' and index >= 0:
                index -= 1
            result = self.pop_words(s[:index+1], result)
        return result

    def reverseWords(self, s: str) -> str:
        result = ''
        index = len(s)-1
        while s[index] == ' ' and index >= 0:
            index -= 1
        result = self.pop_words(s[:index+1], result)
        return result[:-1]
            
class Solution_API:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


s = "  "
S = Solution()
print(S.reverseWords(s))
