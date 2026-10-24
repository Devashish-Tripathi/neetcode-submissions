class MedianFinder:

    def __init__(self):
        self.first, self.second = [], []

    def addNum(self, num: int) -> None:
        if self.second and num > self.second[0]:
            heapq.heappush(self.second, num)
        else:
            heapq.heappush(self.first, -num)
        if len(self.first) > len(self.second) + 1:
            heapq.heappush(self.second, -heapq.heappop(self.first))
        if len(self.second) > len(self.first) + 1:
            heapq.heappush(self.first, -heapq.heappop(self.second))


    def findMedian(self) -> float:
        if len(self.first) == len(self.second):
            return (-self.first[0]+self.second[0])/2
        elif len(self.first) > len(self.second):
            return -self.first[0]
        else:
            return self.second[0]
        