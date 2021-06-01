from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x : x[1], reverse=True)

        totalUnits = 0

        for numBox, unit in boxTypes:
            if truckSize <= numBox:
                totalUnits += truckSize * unit
                break
            totalUnits += numBox * unit
            truckSize -= numBox
        return totalUnits


if __name__ == "__main__":
    s = Solution()
    s.maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4)