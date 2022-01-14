from heapq import heappush, heappop
from collections import defaultdict
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        value_idx = defaultdict(list)
        stack = []
        for i, v in enumerate(nums2):
            value_idx[v+nums1[0]].append([0, i])
            heappush(stack, v+nums1[0])
        while len(result) < k and stack:
            value = heappop(stack)
            idx1, idx2 = value_idx[value].pop()
            result.append([nums1[idx1], nums2[idx2]])
            if idx1 < len(nums1)-1:
                idx1 += 1
                v = nums2[idx2]
                value_idx[v+nums1[idx1]].append([idx1, idx2])
                heappush(stack, v+nums1[idx1])
        return result