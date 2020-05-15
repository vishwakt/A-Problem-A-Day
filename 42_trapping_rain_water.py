from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        print(height)

        if height is None or len(height) == 0:
            return 0

        totalTrapped = 0
        leftHigh = [0] * len(height)
        rightHigh = [0] * len(height)
        leftHigh[0] = height[0]
        rightHigh[-1] = height[-1]

        for i in range(1, len(height)):
            leftHigh[i] = max(leftHigh[i-1], height[i])

        for i in range(len(height)-2, -1, -1):
            rightHigh[i] = max(rightHigh[i+1], height[i])

        for i in range(len(height)):
            totalTrapped += min(leftHigh[i], rightHigh[i]) - height[i]

        return totalTrapped


if __name__ == "__main__":
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
