class Solution:
    def local_search(self, board, i, j, pre, char_list):
        if '*' in char_list:
            self.result.add(pre)
        if i-1 >= 0 and board[i-1][j] in char_list:
            temp = board[i-1][j]
            board[i-1][j] = '#'
            next_char_list = self.word_dict[pre+temp]
            self.local_search(board, i-1, j, pre+temp, next_char_list)
            board[i-1][j] = temp
        if j-1 >= 0 and board[i][j-1] in char_list:
            temp = board[i][j-1]
            board[i][j-1] = '#'
            next_char_list = self.word_dict[pre+temp]
            self.local_search(board, i, j-1, pre+temp, next_char_list)
            board[i][j-1] = temp
        if i+1 <= self.M-1 and board[i+1][j] in char_list:
            temp = board[i+1][j]
            board[i+1][j] = '#'
            next_char_list = self.word_dict[pre+temp]
            self.local_search(board, i+1, j, pre+temp, next_char_list)
            board[i+1][j] = temp
        if j+1 <= self.N-1 and board[i][j+1] in char_list:
            temp = board[i][j+1]
            board[i][j+1] = '#'
            next_char_list = self.word_dict[pre+temp]
            self.local_search(board, i, j+1, pre+temp, next_char_list)
            board[i][j+1] = temp


    def findWords(self, board, words):
        from collections import defaultdict
        self.word_dict = defaultdict(set)
        for word in words:
            self.word_dict[word].add('*')
            for i in range(1,len(word)):
                self.word_dict[word[0:i]].add(word[i])

        self.result = set()
        self.M = len(board)
        self.N = len(board[0])
        for i in range(self.M):
            for j in range(self.N):
                if board[i][j] in self.word_dict:
                    temp = board[i][j]
                    board[i][j] = '#'
                    next_char_list = self.word_dict[temp]
                    self.local_search(board, i, j, temp, next_char_list)
                    board[i][j] = temp

        return list(self.result)