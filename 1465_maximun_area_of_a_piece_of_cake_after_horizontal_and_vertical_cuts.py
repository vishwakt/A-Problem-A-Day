from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        maxHorizontal = 0
        maxVertical = 0

        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)

        horizontalCuts.append(h)
        verticalCuts.append(w)

        horizontalCuts = [0] + horizontalCuts
        verticalCuts = [0] + verticalCuts

        for i in range(1, len(horizontalCuts)):
            maxHorizontal = max(horizontalCuts[i] - horizontalCuts[i-1], maxHorizontal)

        for j in range(1, len(verticalCuts)):
            maxVertical = max(verticalCuts[j] - verticalCuts[j-1], maxVertical)

        return maxVertical * maxHorizontal % 1000000007


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea(h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]))