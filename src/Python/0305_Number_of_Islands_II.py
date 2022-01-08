from collections import defaultdict
class Solution:
    def numIslands2(self, m: int, n: int, positions):
        pos_index_map = {}
        index_pos_map = defaultdict(list)
        count = 0
        result = []
        for i, [row, column] in enumerate(positions):
            if not (row, column) in pos_index_map:
                neighbors = [(row-1, column), (row+1, column), (row, column+1), (row, column-1)]
                island = set()
                for neighbor in neighbors:
                    if neighbor in pos_index_map:
                        island.add(pos_index_map[neighbor])
                island = list(island)
                if island:
                    count -= (len(island)-1)
                    idx = island[0]
                    index_pos_map[idx].append((row, column))
                    pos_index_map[(row, column)] = idx
                    for j in island[1:]:
                        along_island = index_pos_map.pop(j)
                        index_pos_map[idx].extend(along_island)
                        for k in along_island:
                            pos_index_map[k] = idx
                else:
                    index_pos_map[i].append((row, column))
                    pos_index_map[(row, column)] = i
                    count += 1
            result.append(count)
        return result
