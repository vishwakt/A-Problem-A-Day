from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        timeDict = [0] * 60
        pairs = 0

        for t in time:
            timeDict[t % 60] += 1

        # print(timeDict)
        for i in range(31):
            if i == 0 or i == 30:
                n = timeDict[i]
                pairs += n * (n - 1) // 2
            else:
                pairs += timeDict[i] * timeDict[60 - i]
        return pairs


if __name__ == "__main__":
    s = Solution()
    print(s.numPairsDivisibleBy60(time = [30,20,150,100,40]))