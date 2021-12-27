class Solution:
    def getSkyline(self, buildings):
        result = [[-1, 0]]
        for build in buildings:
            left = build[0]
            right = build[1]
            height = build[2]
            if result:
                if left > result[-1][0]:
                    result.extend([[left, height], [right, 0]])
                elif left == result[-1][0]:
                    result.pop()
                    result.extend([[left, height], [right, 0]])
                else:
                    conor = []
                    while result[-1][0] >= left:
                        if result[-1][0] >= right:
                            end = result.pop()
                            conor.append(end)
                        else:
                            if result[-1][1] > height:
                                end = result.pop()
                                right = end[0]
                                conor.append(end)
                            elif result[-1][1] <= height:
                                conor.append([right, result[-1][1]])
                                conor.append([result[-1][0], height])
                                right = result[-1][0]
                                end = result.pop()
                    if result[-1][1] < height:
                        result.append([left, height])
                        result.append([right, result[-2][1]])
                    result.extend(conor[::-1])                    
                    
            else:
                result.extend([[left, height], [right, 0]])

        final_result = []
        while result:
            if final_result:
                if final_result[-1][0] == result[-1][0]:
                    result.pop()
                elif final_result[-1][1] == result[-1][1]:
                    final_result.pop()
                    final_result.append(result.pop())
                else:
                    final_result.append(result.pop())
            else:
                final_result.append(result.pop())
        return final_result[::-1][1:]