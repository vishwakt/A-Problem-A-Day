import heapq
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        totalCost = 0
        while len(sticks) > 1:
            a = heapq.heappop(sticks)
            b = heapq.heappop(sticks)
            c = a + b
            totalCost += c
            heapq.heappush(sticks, c)
        return totalCost


if __name__ == "__main__":
    s = Solution()
    print(s.connectSticks(sticks = [1,8,3,5]))


