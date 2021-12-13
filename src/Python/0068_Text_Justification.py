from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []
        length_words = 0
        count_words = 0
        for i in words:
            if length_words+len(i)+count_words > maxWidth:
                if count_words == 1:
                    result.append(line[0] + ' '*(maxWidth-length_words))
                else:
                    line_result = line[0]
                    space_base = (maxWidth-length_words)//(count_words-1)
                    space_mod = (maxWidth-length_words)%(count_words-1)
                    for j in line[1:]:
                        line_result += ' '*space_base
                        if space_mod > 0:
                            line_result += ' '
                            space_mod -= 1
                        line_result += j
                    result.append(line_result)
                line = [i]
                length_words = len(i)
                count_words = 1
            else:
                count_words += 1
                length_words += len(i)
                line.append(i)
        line_result = line[0]
        for i in line[1:]:
            line_result += (' '+i)
        line_result += ' '*(maxWidth-length_words-count_words+1)
        result.append(line_result)
        return result
        
                    