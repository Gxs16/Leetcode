from collections import defaultdict


class Solution:
    def isTrans(self, base_word, target_word) -> bool:
        count = 0
        for i, char in enumerate(base_word):
            if char != target_word[i]:
                if count == 1:
                    return False
                else:
                    count += 1
        if count == 1:
            return True
        else:
            return False

    def findLadders(self, beginWord: str, endWord: str, wordList):
        if endWord not in wordList:
            return []
        trans_dict = {beginWord: [[beginWord]]}
        used = [beginWord]
        is_break=False
        while trans_dict:
            trans_dict_new = defaultdict(list)
            for key, path_list in trans_dict.items():
                for word in wordList:
                    if word in used:
                        continue
                    else:
                        if self.isTrans(key, word):
                            for path in path_list:
                                trans_dict_new[word].append(path+[word])
                            if word == endWord:
                                is_break=True
            used.extend(trans_dict_new.keys())
            trans_dict = trans_dict_new
            if is_break:
                break
        return trans_dict[endWord]