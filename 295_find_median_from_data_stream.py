import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smallNumbers, self.largeNumbers = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallNumbers, -1 * num)

        if self.smallNumbers and self.largeNumbers and ((-1 * self.smallNumbers[0]) > self.largeNumbers[0]):
            val = -1 * heapq.heappop(self.smallNumbers)
            heapq.heappush(self.largeNumbers, val)

        # If heaps are of uneven size
        if len(self.smallNumbers) > len(self.largeNumbers) + 1:
            val = -1 * heapq.heappop(self.smallNumbers)
            heapq.heappush(self.largeNumbers, val)

        if len(self.smallNumbers) + 1 < len(self.largeNumbers):
            val = -1 * heapq.heappop(self.largeNumbers)
            heapq.heappush(self.smallNumbers, val)

    def findMedian(self) -> float:
        if len(self.smallNumbers) > len(self.largeNumbers):
            return -1 * self.smallNumbers[0]
        if len(self.smallNumbers) < len(self.largeNumbers):
            return self.largeNumbers[0]

        return (-1 * self.smallNumbers[0] + self.largeNumbers[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()