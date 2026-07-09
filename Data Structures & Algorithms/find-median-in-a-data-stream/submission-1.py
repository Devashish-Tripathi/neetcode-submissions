class MedianFinder:

    def __init__(self):
        self.nums = []
        self.nums_size = 0
        self.med_idx1 = 0
        self.med_idx2 = 0

    def addNum(self, num: int) -> None:
        
        self.nums.append(num)
        self.nums = sorted(self.nums)
        self.nums_size += 1
        self.med_idx1 = self.nums_size//2
        self.med_idx2 = self.med_idx1-1
    
    
    def findMedian(self) -> float:
        if self.nums_size % 2:
            return self.nums[self.med_idx1]
        else:
            return (self.nums[self.med_idx1]+self.nums[self.med_idx2])/2
        