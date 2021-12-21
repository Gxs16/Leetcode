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
        if count == 0:
            return False

    def next_ladder(self, beginWord, endWord, wordList, used):
        min_path = float('inf')
        candidate = set()
        _path = 0
        for word in wordList:
            if word in used:
                continue
            if self.isTrans(beginWord, word):
                candidate.add(word)
        if endWord in candidate:
            return 1
        for can in candidate:
            used_next = used.copy()
            used_next.add(can)
            _path = (self.next_ladder(can, endWord, wordList, used_next))
            if _path:
                min_path = min(min_path, _path)
        if _path == float('inf'):
            return False
        else:
            return _path+1
        
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        min_path = float('inf')
        _path = 0
        if endWord in wordList:
            candidate = set()
            for word in wordList:
                if self.isTrans(beginWord, word):
                    candidate.add(word)
            if candidate:
                if endWord in candidate:
                    return 2
                for can in candidate:
                    used = set()
                    _path = (self.next_ladder(can, endWord, wordList, used))
                    if _path:
                        min_path = min(min_path, _path)
            if _path == float('inf'):
                return False
            else:
                return _path+1
        else:
            return 0