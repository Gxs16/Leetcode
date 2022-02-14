class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        count = 0
        j = -1
        for char in target:
            start = j+1
            for j in range(start, len(source)):
                if source[j] == char:
                    break
            else:
                count += 1
                for j in range(start):
                    if source[j] == char:
                        break
                else:
                    return -1
        return count+1
            
if __name__ == '__main__':
    print(Solution().shortestWay("abc",
"abcbc"))