from heapq import heappush, heappop
class Solution:
    def __init__(self):
        self.result = []
        self.record = {}
        self.heap_min = []
        self.heap_max = []
        self.num_min = 0
        self.num_max = 0

    def update_record(self, num):
        if num in self.record:
            self.record[num] += 1
        else:
            self.record[num] = 1

    def input_num(self, num):
        if self.heap_max:
            if num <= -self.heap_max[0]:
                heappush(self.heap_max, -num)
                self.num_max += 1
                if self.num_max > self.num_min+1:
                    heappush(self.heap_min, -heappop(self.heap_max))
                    self.num_max -= 1
                    self.num_min += 1
            else:
                heappush(self.heap_min, num)
                self.num_min += 1
                if self.num_max < self.num_min:
                    heappush(self.heap_max, -heappop(self.heap_min))
                    self.num_max += 1
                    self.num_min -= 1
        else:
            self.heap_max.append(-num)
            self.num_max += 1

    def get_median(self):
        
        if self.num_max == self.num_min:
            self.result.append((-self.heap_max[0]+self.heap_min[0])/2)
        else:
            self.result.append(-self.heap_max[0])

    def medianSlidingWindow(self, nums, k: int):
        if k == 1:
            return nums
        for i in range(k):
            self.input_num(nums[i])
        self.get_median()

        for j in range(k, len(nums)):
            left = nums[j-k]
            right = nums[j]
            self.update_record(left)
            if left == -self.heap_max[0]:
                self.num_max -= 1
                self.record[left] -= 1
                heappop(self.heap_max)
                while self.num_max < self.num_min:
                    cur = heappop(self.heap_min)
                    if cur not in self.record or self.record[cur] == 0:
                        heappush(self.heap_max, -cur)
                        self.num_max += 1
                        self.num_min -= 1
                    else:
                        self.record[cur] -= 1
            elif left < -self.heap_max[0]:
                self.num_max -= 1
                while self.num_max < self.num_min:
                    cur = heappop(self.heap_min)
                    if cur not in self.record or self.record[cur] == 0:
                        heappush(self.heap_max, -cur)
                        self.num_max += 1
                        self.num_min -= 1
                    else:
                        self.record[cur] -= 1
            else:
                self.num_min -= 1
                while self.num_max > self.num_min+1:
                    cur = -heappop(self.heap_max)
                    if cur not in self.record or self.record[cur] == 0:
                        heappush(self.heap_min, cur)
                        self.num_max -= 1
                        self.num_min += 1
                    else:
                        self.record[cur] -= 1
            self.input_num(right)
            while -self.heap_max[0] in self.record and self.record[-self.heap_max[0]] > 0:
                self.record[-self.heap_max[0]] -= 1
                heappop(self.heap_max)
            while self.heap_min[0] in self.record and self.record[self.heap_min[0]] > 0:
                self.record[self.heap_min[0]] -= 1
                heappop(self.heap_min)
            self.get_median()
        return self.result

if __name__ == '__main__':
    Solution().medianSlidingWindow([1,1,1,1],2)