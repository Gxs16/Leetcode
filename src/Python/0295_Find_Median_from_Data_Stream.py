import heapq
class MedianFinder:

    def __init__(self):
        self.heap_max = []# 存储小于等于中位数的值
        self.heap_min = []# 存储大于中位数的值


    def addNum(self, num: int) -> None:
        if self.heap_max:
            if num <= -self.heap_max[0]: # 小于当前中位数
                heapq.heappush(self.heap_max, -num)
                if len(self.heap_max) > len(self.heap_min)+1:
                    heapq.heappush(self.heap_min, -heapq.heappop(self.heap_max))
            else:
                heapq.heappush(self.heap_min, num)
                if len(self.heap_min) > len(self.heap_max):
                    heapq.heappush(self.heap_max, -heapq.heappop(self.heap_min))
        else:
            self.heap_max.append(-num)


    def findMedian(self) -> float:
        if len(self.heap_max) == len(self.heap_min):
            return (-self.heap_max[0]+self.heap_min[0])/2
        else:
            return -self.heap_max[0]
