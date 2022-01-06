class Solution:
    def getCount(self, prefix, n):
        count = 0
        cur_node = prefix
        next_node = prefix+1
        while cur_node <= n:
            count += min(next_node, n+1) - cur_node
            cur_node *= 10
            next_node *= 10

    def findKthNumber(self, n: int, k: int) -> int:
        rank = 1
        cur_node = 1
        while rank < k:
            count = self.getCount(cur_node, n)
            if rank + count > k:
                cur_node *= 10
                rank += 1
            else:
                cur_node += 1
                rank += count
        return cur_node
        
        