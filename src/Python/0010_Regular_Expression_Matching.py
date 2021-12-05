'''
@Author: Xinsheng Guo
@Time: 2021年12月5日
@File: 0010_Regular_Expression_Matching.py
@Link: https://leetcode-cn.com/problems/regular-expression-matching/
'''
#%%
class Solution:
    def isNormalMatch(self, s, p):
        if len(s) != len(p):
            return False
        for i, j in zip(s, p):
            if j != '.' and i!=j:
                return False
        return True

    def isStarMatch(self, s, p_star, p_list):
        if p_list:
            if p_star == '.':
                for i in range(len(s)):
                    if self.isUnitMatch(s[i:], p_list):
                        return True
                return self.isUnitMatch('', p_list)
            else:
                for i in range(len(s)):
                    if self.isUnitMatch(s[i:], p_list):
                        return True
                    else:
                        if s[i] != p_star:
                            return False
                return self.isUnitMatch('', p_list)
        elif not p_list:
            if p_star == '.':
                return True
            else:
                return p_star*len(s) == s

    def isUnitMatch(self, s, p_list):
        if p_list and s:
            p = p_list[0]
            p_list = p_list[1:]
            if len(p) == 1:
                return self.isStarMatch(s, p, p_list)
            else:
                p_normal = p[:-1]
                p_star = p[-1]
                s_normal = s[:len(p_normal)]
                s_left = s[len(p_normal):]
                if self.isNormalMatch(s_normal, p_normal):
                    return self.isStarMatch(s_left, p_star, p_list)
                else:
                    return False
        elif not p_list and s:
            return False
        elif p_list and not s:
            for i in p_list:
                if len(i) > 1:
                    return False
            return True
        else:
            return True
        
    def isMatch(self, s: str, p: str) -> bool:
        p_list = p.split('*')
        if p_list[-1] != '':
            string = s[-len(p_list[-1]):]
            s = s[:-len(p_list[-1])]
            if not self.isNormalMatch(string, p_list[-1]):
                return False
        p_list = p_list[0:-1]
        return self.isUnitMatch(s, p_list)

#%%
Solution().isMatch(s="aaa", p="ab*a*c*a")
# %%
Solution().isMatch(s="a", p="ab*a")
# %%
