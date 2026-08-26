import heapq as hq
class MedianFinder:
    def __init__(self):
        self.minh = []
        self.maxh = []

    def addNum(self, num: int) -> None:
        hq.heappush(self.minh, num)

        if len(self.minh) - len(self.maxh) > 1:
            hq.heappush(self.maxh, -hq.heappop(self.minh))
        
        if len(self.maxh) and -self.maxh[0] > self.minh[0]:
            self.maxh[0], self.minh[0] = -self.minh[0], -self.maxh[0]

    def findMedian(self) -> float:
        if len(self.minh) - len(self.maxh) == 1:
            return self.minh[0]
        return (self.minh[0] - self.maxh[0]) / 2

        
        