class Solution:
    def isTrans(self, base_word, target_word) -> bool:
        count = 0
        for i, char in enumerate(base_word):
            if char != target_word[i]:
                count += 1
            if count > 1:
                return False
        if count == 1:
            return True

    def nextCandidate(self, endWord, used, candidate):
        candidate_next = []
        for cand in candidate:
            for word in used:
                if used[word] == 0:
                    continue
                if self.isTrans(cand, word):
                    if endWord == word:
                        return 2
                    candidate_next.append(word)
                    used[word] -= 1
        if candidate_next:
            path = self.nextCandidate(endWord, used, candidate_next)
            if path:
                return path+1
            else:
                return False
        else:
            return False

    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        candidate = []
        used = {}
        for word in wordList:
            used[word] = 1
            if self.isTrans(beginWord, word):
                if endWord == word:
                    return 2
                candidate.append(word)
                used[word] -= 1
        used[beginWord] = 0
        path = self.nextCandidate(endWord, used, candidate)
        if path:
            return path+1
        else:
            return 0
